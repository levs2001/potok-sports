# Потоковый анализ данных. Л1

## Входные данные

Данные о голах, карточках, ударах, ...
https://allsportsapi.com/soccer-football-socket-documentation

Пример сообщения:

```
[
  {
        "event_key": "11205",
        "event_date": "2021-05-21",
        "event_time": "11:05",
        "event_home_team": "Newcastle Jets",
        "home_team_key": "1056",
        "event_away_team": "Brisbane Roar",
        "away_team_key": "399",
        "event_halftime_result": "0 - 1",
        "event_final_result": "1 - 2",
        "event_ft_result": "1 - 2",
        "event_penalty_result": "",
        "event_status": "74",
        "country_name": "Australia",
        "league_name": "A-League - Regular Season",
        "league_key": "49",
        "league_round": "22",
        "league_season": "",
        "event_live": "1",
        "event_stadium": "McDonald Jones Stadium",
        "event_referee": "",
        "event_country_key": "17",
        "league_logo": "https://apiv2.allsportsapi.com/logo/logo_leagues/49_a-league.png",
        "country_logo": "https://apiv2.allsportsapi.com/logo/logo_country/17_australia.png",
        "event_home_formation": "",
        "event_away_formation": "",
        "fk_stage_key": "528",
        "stage_name": "Regular Season",
        "goalscorers": [
            {
                "time": "34",
                "home_scorer": "",
                "score": "0 - 1",
                "away_scorer": "R. Danzaki"
            },
            {
                "time": "61",
                "home_scorer": "J. O'Shea (o.g.)",
                "score": "1 - 1",
                "away_scorer": ""
            },
            {
                "time": "73",
                "home_scorer": "",
                "score": "1 - 2",
                "away_scorer": "J. O'Shea"
            }
        ],
        "cards": [
            {
                "time": "21",
                "home_fault": "",
                "card": "yellow card",
                "away_fault": "M. Gillesphey"
            },
            {
                "time": "42",
                "home_fault": "J. Hoffman",
                "card": "yellow card",
                "away_fault": ""
            },
            ........................
        ],
        "substitutes": [
            {
                "time": "46",
                "home_scorer": {
                    "in": "C. O'Toole",
                    "out": "L. Mauragis"
                },
                "score": "substitution",
                "away_scorer": []
            },
            {
                "time": "46",
                "home_scorer": {
                    "in": "A. Abbas",
                    "out": "A. Goodwin"
                },
                "score": "substitution",
                "away_scorer": []
            },
            ..............
        ],
        "lineups": {
            "home_team": {
                "starting_lineups": [
                    {
                        "player": "Jack Duncan",
                        "player_number": "23",
                        "player_country": null
                    },
                    {
                        "player": "Johnny Koutroumbis",
                        "player_number": "2",
                        "player_country": null
                    },
                    .......................
                ],
                "substitutes": [
                    {
                        "player": "Lewis Italiano",
                        "player_number": "1",
                        "player_country": null
                    },
                    .................
                ],
                "coaches": [
                    {
                        "coache": "W. Moon",
                        "coache_country": null
                    }
                ]
            }
        },
        "statistics": [
            {
                "type": "Shots Blocked",
                "home": "1",
                "away": "6"
            }
            ..................
        ]
  },
  .......
]
```

```
goalscorers - забившие голы.
goalscorers.home_scorer - игрок забивщий из домашней команды
goalscorers.away_scorer - игрок забивщий из команды на выезде
event_home_team - домашняя команда
event_away_team - команда на выезде
```

## Конечная цель:

Дашборд с разбиением по лигам с топовыми бомбардирами

```
English Premier league:
    De Bruyne: 10
    Harry Cane: 8
    ...
    
La ligue:
    Robert Levandovskiy: 15
    Kilian Mbappe: 10
    
```

Необходимо отсеивать дубликатов и учитывать тесок по клубам.