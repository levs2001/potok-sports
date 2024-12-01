package ru.leo.potok;

import org.apache.flink.connector.base.DeliveryGuarantee;
import org.apache.flink.connector.kafka.sink.KafkaSink;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import ru.leo.potok.serial.FootballEventDeserializer;
import ru.leo.potok.domain.FootballEvent;
import ru.leo.potok.domain.ResultFootballEvent;
import ru.leo.potok.serial.ResultFootballEventSerizlizer;

public class KafkaUtils {
    public static KafkaSource<FootballEvent> createKafkaSource(String topic, String kafkaAddress, String kafkaGroup) {
        return KafkaSource.<FootballEvent>builder()
            .setBootstrapServers(kafkaAddress)
            .setGroupId(kafkaGroup)
            .setTopics(topic)
            .setValueOnlyDeserializer(new FootballEventDeserializer())
            .setStartingOffsets(OffsetsInitializer.earliest())
            .build();
    }

    public static KafkaSink<ResultFootballEvent> createKafkaSink(String topic, String kafkaAddress) {
        return KafkaSink.<ResultFootballEvent>builder()
            .setBootstrapServers(kafkaAddress)
            .setRecordSerializer(new ResultFootballEventSerizlizer(topic))
            .setDeliveryGuarantee(DeliveryGuarantee.AT_LEAST_ONCE)
            .build();
    }
}
