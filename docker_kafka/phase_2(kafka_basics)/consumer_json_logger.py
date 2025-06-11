from kafka import KafkaConsumer
import json

# Connect to Kafka topic
consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers='localhost:9092',
    group_id='json-log-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)
print("Listening for messages...")

# Open file in append mode
with open('logs.jsonl', 'a') as logfile:
    print("Consumer is logging messages to logs.jsonl ...")
    for message in consumer:
        log_entry = message.value
        
        # Print to console
        print(f"Received: {log_entry}")
        
        # Write JSON as one line to file
        logfile.write(json.dumps(log_entry) + '\n')
        logfile.flush()  # ensures it writes immediately
