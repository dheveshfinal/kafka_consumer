from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    group_id='group1',
    auto_offset_reset='earliest'
)

print("Consumer 1 started...")
for message in consumer:
    print(f"[Consumer 1] {message.value.decode('utf-8')}")
