package ru.leo.potok.domain;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

@Data
@JsonIgnoreProperties(ignoreUnknown = true)
public class FootballEvent {
    @JsonProperty("event_type")
    private String eventType;

    @JsonProperty("league")
    private String league;

    @JsonProperty("teams")
    private String teams;

    @JsonProperty("goal_author_team")
    private String goalAuthorTeam;

    @JsonProperty("missed_goal_team")
    private String missedGoalTeam;
}
