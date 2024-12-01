package ru.leo.potok;

import lombok.extern.log4j.Log4j2;
import org.apache.flink.streaming.api.functions.windowing.ProcessWindowFunction;
import org.apache.flink.streaming.api.windowing.windows.TimeWindow;
import org.apache.flink.util.Collector;
import ru.leo.potok.domain.FootballEvent;
import ru.leo.potok.domain.FootballEventKey;
import ru.leo.potok.domain.ResultFootballEvent;

@Log4j2
public class AggregateMatchFunction
    extends ProcessWindowFunction<FootballEvent, ResultFootballEvent, FootballEventKey, TimeWindow> {
    private static final String GOAL = "goal";
    private static final String TEAMS_SPLITTER = " - ";

    @Override
    public void process(
        FootballEventKey key,
        Context context,
        Iterable<FootballEvent> input,
        Collector<ResultFootballEvent> out
    ) {
        int t1Score = 0;
        int t2Score = 0;
        String t1Name = key.getTeams().split(TEAMS_SPLITTER)[0];
        for (FootballEvent e : input) {
            if (e.getEventType().equals(GOAL)) {
                if (e.getMissedGoalTeam().equals(t1Name)) {
                    t2Score++;
                } else {
                    t1Score++;
                }
            }
        }

        var result = new ResultFootballEvent(
            context.currentProcessingTime(),
            key.getLeague(),
            key.getTeams(),
            String.format("%d - %d", t1Score, t2Score)
        );

        log.info("Collecting match result: {}", result);

        out.collect(result);
    }
}