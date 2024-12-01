package ru.leo.potok.domain;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

@Data
public class ResultFootballEvent {
    @JsonProperty("end_timestamp")
    private final long endTimestamp;

    @JsonProperty("league")
    private final String league;

    @JsonProperty("teams")
    private final String teams;

    @JsonProperty("result_score")
    private final String resultScore;
}
