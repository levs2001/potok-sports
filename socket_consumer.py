import json
import asyncio
import websockets


async def connect(uri: str):
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)[0]
            print(data)
            with open("res.json", "a") as f:
                f.write(message)
            if len(data["goalscorers"]) > 0:
                with open("goal_scorers.json", "a") as f:
                    for goal in data["goalscorers"]:
                        f.write(goal["away_scorer"] + "\n")


async def main():
    uri = ("wss://wss.allsportsapi.com/live_events?"
           "APIkey=1b9ce5034452d1c11dd73530a0a647a8306c2cea45ec46c77bbdf87fec7a5da2"
           "&timezone=Europe/Moscow")
    await connect(uri)


asyncio.run(main())
