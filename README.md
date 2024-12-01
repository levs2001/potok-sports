# Потоковый анализ данных. 

## Входные данные

Данные о начале матча, конце матче, голах генерируются с помощью [генератора](./generator/match_event_generator.py)
и пишутся в web socket.

### Примеры сообщений

Старт матча:

```
{
    "event_type": "match_start",
    "league": "Premier League",
    "teams": "Tottenham Hotspur - Manchester United"
}
```

Гол:

```
{
    "event_type": "goal",
    "league": "Premier League",
    "teams": "Tottenham Hotspur - Manchester United",
    "goal_author_team": "Manchester United",
    "missed_goal_team": "Tottenham Hotspur"
}
```

Конец матча:

```
{
    "event_type": "match_end",
    "league": "Premier League",
    "teams": "Tottenham Hotspur - Manchester United"
}
```

## Конечная цель:

Статистика со счетом по всем завершенным матчам:

```
Premier League:
    
    end time: 19/10/24 : 20:00 
    commands: Tottenham Hotspur - Manchester United
    score: 2 : 0 
    ...

Bundesliga:
    end time: 19/10/24 : 20:00 
    commands: Koln - Mainz
    score: 2 : 0 
        
```
