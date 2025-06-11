from kafka import KafkaConsumer
import json
import mysql.connector

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',     # ✅ replace with your username
    password='12345', # ✅ replace with your password
    database='kafka_logs'
)
cursor = conn.cursor()

# Step 2: Create table if not exists (run once)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_logs (
        user_id INT,
        name VARCHAR(255),
        action VARCHAR(255)
    )
''')
conn.commit()

# Step 3: Set up Kafka consumer
consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers='localhost:9092',
    group_id='mysql-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Listening for messages on 'user-events'...")

for message in consumer:
    data = message.value
    print(f"Received: {data}")

    # Step 4: Insert into MySQL
    insert_query = 'INSERT INTO user_logs (user_id, name, action) VALUES (%s, %s, %s)'
    values = (data['user_id'], data['name'], data['action'])

    cursor.execute(insert_query, values)
    conn.commit()
