package ru.leo.potok;

import java.time.Duration;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.EventTimeSessionWindows;
import ru.leo.potok.domain.FootballEvent;
import ru.leo.potok.domain.FootballEventKey;

public class Process {
    private static final String INPUT_TOPIC = "football_events";
    private static final String OUTPUT_TOPIC = "football_results";
    private static final String consumerGroup = "baeldung";
    private static final String address = "localhost:9092,localhost:9093,localhost:9094";

    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment environment = StreamExecutionEnvironment.getExecutionEnvironment();
        var source = KafkaUtils.createKafkaSource(INPUT_TOPIC, address, consumerGroup);

        DataStream<FootballEvent> stringInputStream = environment
            .fromSource(source,
                WatermarkStrategy
                    .<FootballEvent>forBoundedOutOfOrderness(Duration.ofSeconds(1))
                    .withTimestampAssigner((element, recordTimestamp) -> recordTimestamp),
                "Football events Source"
            )
            .setParallelism(1);

        var sink = KafkaUtils.createKafkaSink(OUTPUT_TOPIC, address);

        stringInputStream
            .keyBy(e -> new FootballEventKey(e.getLeague(), e.getTeams()))
            .window(EventTimeSessionWindows.withGap(Duration.ofSeconds(10)))
            .process(new AggregateMatchFunction())
            .sinkTo(sink);

        environment.execute("Match processer");
    }
}
