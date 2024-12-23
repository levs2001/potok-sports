import asyncio
import json
from datetime import datetime

import websockets
from kafka import KafkaConsumer, TopicPartition

connected_clients = set()

topic_name = "football_results"
consumer = KafkaConsumer(topic_name,
                         bootstrap_servers=['localhost:9092'],
                         group_id=None,
                         # auto_commit_enable=False,
                         auto_offset_reset='latest')


async def send_messages():
    print("Consuming messages from the given topic")
    key_part = TopicPartition(topic=topic_name, partition=0)
    while True:
        messages = consumer.poll(1000)
        if key_part in messages:
            for message in messages[key_part]:
                if message is not None:
                    message = json.loads(message.value)
                    message["end_timestamp"] = int(datetime.now().timestamp() * 1000)
                    message = json.dumps(message)
                    print(message)
                    await broadcast(message)
        await asyncio.sleep(1)


async def broadcast(message):
    if connected_clients:  # asyncio.wait doesn't accept an empty list
        await asyncio.gather(*[client.send(message) for client in connected_clients])


async def echo(websocket, path):
    connected_clients.add(websocket)
    print(f"Conntected clints: {connected_clients}")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")
    finally:
        print(f"Removed ws: {websocket}")
        connected_clients.remove(websocket)


async def main():
    server = await websockets.serve(echo, "localhost", 8764)
    # await server.wait_closed()
    # await send_messages()
    await asyncio.gather(send_messages(), server.wait_closed())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        consumer.close()
