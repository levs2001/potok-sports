import random
import time
import json

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


def generate_match_event() -> str:
    # Select a random league
    league = random.choice(list(leagues.keys()))

    # Select two random teams from the chosen league
    teams = random.sample(leagues[league], 2)

    # Simulate a goal event
    old_score = "0 - 0"
    new_score = "1 - 0" if random.choice([True, False]) else "0 - 1"

    # Create the event dictionary
    event = {
        "event_type": "goal",
        "league": league,
        "teams": f"{teams[0]} - {teams[1]}",
        "old_score": old_score,
        "new_score": new_score
    }

    # Print the event in JSON format
    return json.dumps(event, indent=2)
