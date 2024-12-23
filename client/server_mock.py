import asyncio
import json
from datetime import datetime
import ast

import websockets
import random

connected_clients = set()

MESSAGES = [
    '{"end_timestamp":1734946218271,"league":"Premier League","teams":"Newcastle United - Chelsea","result_score":"0 - 0"}',
    '{"end_timestamp":1734946218272,"league":"Ligue 1","teams":"Lille - Angers","result_score":"0 - 0"}',
    '{"end_timestamp":1734946218275,"league":"Bundesliga","teams":"Stuttgart - Werder Bremen","result_score":"1 - 0"}'
]


async def send_messages():
    while True:
        # message = f"Random number: {random.randint(1, 100)}"
        message = MESSAGES[random.randint(0, 2)]
        message = ast.literal_eval(message)
        message["end_timestamp"] = int(datetime.now().timestamp() * 1000)
        message = json.dumps(message)
        print(message)
        if connected_clients:  # asyncio.wait doesn't accept an empty list
            print(connected_clients)
            await asyncio.gather(*[client.send(message) for client in connected_clients])
        await asyncio.sleep(1)  # Send a message every 5 seconds


async def echo(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")
    finally:
        print(f"Removed ws: {websocket}")
        connected_clients.remove(websocket)


async def main():
    server = await websockets.serve(echo, "localhost", 8764)
    await asyncio.gather(server.wait_closed(), send_messages())


if __name__ == "__main__":
    asyncio.run(main())
