from kafka import KafkaProducer
import time

# Connect to Kafka broker
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send 5 sample messages
for i in range(5):
    message = f"Hello Kafka! Message {i}"
    producer.send('test-topic', value=message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)

producer.close()
