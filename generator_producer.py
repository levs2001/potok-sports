import time

from generator.match_event_generator import generate_match_event
from confluent_kafka import Producer

FLUSH_THRESHOLD = 10


def main():
    topic = 'football_events'

    producer = Producer({
        'bootstrap.servers': 'localhost:9092'
    })

    while True:
        for i in range(FLUSH_THRESHOLD):
            event = generate_match_event()
            print(event)
            producer.produce(topic=topic, value=event.encode('utf-8'))

            print("Waiting...")
            time.sleep(1)
        print("Flushing...")
        producer.flush()
        print("Flushed")


if __name__ == '__main__':
    main()
