from kafka import KafkaProducer
import json
import time

# Set up Kafka producer to serialize JSON
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample JSON messages
users = [
    {"user_id": 1, "name": "Alice", "action": "login"},
    {"user_id": 2, "name": "Bob", "action": "logout"},
    {"user_id": 3, "name": "Charlie", "action": "purchase"},
]
print("Starting producer...")
for user in users:
    producer.send('user-events', value=user)
    print(f"Sent: {user}")
    time.sleep(1)

producer.close()
