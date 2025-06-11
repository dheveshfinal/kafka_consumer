from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    group_id='group1',
    auto_offset_reset='earliest'
)

print("Consumer 2 started...")
for message in consumer:
    print(f"[Consumer 2] {message.value.decode('utf-8')}")
