import asyncio
import websockets

from confluent_kafka import Producer

topic = 'football_events'
producer = Producer({
    'bootstrap.servers': 'localhost:9092'
})


async def handler(websocket, path):
    print("Client connected")

    try:
        async for message in websocket:
            print(f"Received message: {message}")
            producer.produce(topic=topic, value=message.encode('utf-8'))
            # producer.flush(timeout=2)
    except websockets.ConnectionClosed:
        print("Client disconnected")


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
