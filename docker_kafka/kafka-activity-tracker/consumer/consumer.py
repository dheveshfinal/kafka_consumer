from kafka import KafkaConsumer
import json
import mysql.connector
from datetime import datetime

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'user_events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="kafka_log"
)
cursor = db.cursor()

try:
    for message in consumer:
        event = message.value
        print("Received:", event)

        # Convert ISO 8601 timestamp to MySQL-compatible format
        iso_timestamp = event['timestamp']
        dt_obj = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
        mysql_timestamp = dt_obj.strftime("%Y-%m-%d %H:%M:%S")

        # Insert into MySQL
        sql = "INSERT INTO user_activity (user_id, event_type, page, timestamp) VALUES (%s, %s, %s, %s)"
        values = (event['user_id'], event['event_type'], event['page'], mysql_timestamp)
        cursor.execute(sql, values)
        db.commit()
except KeyboardInterrupt:
    print("Consumer stopped by user.")
finally:
    cursor.close()
    db.close()
