import asyncio
import json
import random

import websockets

# Define the leagues and teams
leagues = {
    "Premier League": [
        "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton & Hove Albion",
        "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds United",
        "Leicester City", "Liverpool", "Luton Town", "Manchester City", "Manchester United",
        "Newcastle United", "Nottingham Forest", "Sheffield United", "Tottenham Hotspur",
        "West Ham United", "Wolverhampton Wanderers"
    ],
    "La Liga": [
        "Alaves", "Almeria", "Athletic Bilbao", "Atletico Madrid", "Barcelona", "Cadiz",
        "Celta Vigo", "Elche", "Espanyol", "Getafe", "Girona", "Granada", "Las Palmas",
        "Mallorca", "Osasuna", "Rayo Vallecano", "Real Betis", "Real Madrid", "Real Sociedad",
        "Sevilla", "Valencia", "Villarreal"
    ],
    "Bundesliga": [
        "Augsburg", "Bayer Leverkusen", "Bayern Munich", "Bochum", "Borussia Dortmund",
        "Borussia Monchengladbach", "Darmstadt", "Eintracht Frankfurt", "Freiburg",
        "Heidenheim", "Hoffenheim", "Koln", "Mainz", "RB Leipzig", "Stuttgart",
        "Union Berlin", "Werder Bremen", "Wolfsburg"
    ],
    "Serie A": [
        "Atalanta", "Bologna", "Cagliari", "Empoli", "Fiorentina", "Frosinone", "Genoa",
        "Inter Milan", "Juventus", "Lazio", "Lecce", "AC Milan", "Monza", "Napoli", "Roma",
        "Salernitana", "Sassuolo", "Torino", "Udinese", "Verona"
    ],
    "Ligue 1": [
        "Ajaccio", "Angers", "Auxerre", "Brest", "Clermont", "Le Havre", "Lens", "Lille",
        "Lorient", "Lyon", "Marseille", "Metz", "Monaco", "Montpellier", "Nantes", "Nice",
        "Paris Saint-Germain", "Reims", "Rennes", "Strasbourg", "Toulouse"
    ]
}


async def send_event(websocket, event):
    e = json.dumps(event)
    print(e)
    await websocket.send(e)


async def generate_match_events(websocket, first_goal_wait, other_match_time):
    # Select a random league
    league = random.choice(list(leagues.keys()))

    # Select two random teams from the chosen league
    teams = random.sample(leagues[league], 2)
    event = {
        "event_type": "match_start",
        "league": league,
        "teams": f"{teams[0]} - {teams[1]}",
    }
    await send_event(websocket, event)
    await asyncio.sleep(first_goal_wait)

    goals_count = random.randint(0, 4)
    for i in range(goals_count):
        random.randint(0, 9)
        goal_author_team_b = random.choice([True, False])
        if random.randint(0, 9) == 9:
            # Шанс того, что команда забила в свои ворота 10 процентов.
            missed_goal_team_b = goal_author_team_b
        else:
            missed_goal_team_b = not goal_author_team_b
        event = {
            "event_type": "goal",
            "league": league,
            "teams": f"{teams[0]} - {teams[1]}",
            # Команда забившая гол
            "goal_author_team": teams[int(goal_author_team_b)],
            # Команда в чьи ворота забили
            "missed_goal_team": teams[int(missed_goal_team_b)]
        }
        await send_event(websocket, event)
        await asyncio.sleep(other_match_time / goals_count)
        await send_event(websocket, event)

    if goals_count == 0:
        await asyncio.sleep(other_match_time)
    event = {
        "event_type": "match_end",
        "league": league,
        "teams": f"{teams[0]} - {teams[1]}",
    }
    await send_event(websocket, event)


MATCHES_IN_ONE_TIME = 5
FIRST_GOAL_WAIT = 2
OTHER_MATCH_TIME = 8


async def main():
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            async with asyncio.TaskGroup() as tg:
                for i in range(MATCHES_IN_ONE_TIME):
                    tg.create_task(generate_match_events(websocket, FIRST_GOAL_WAIT, OTHER_MATCH_TIME))
            await asyncio.sleep(10)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
