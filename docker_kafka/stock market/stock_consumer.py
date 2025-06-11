from kafka import KafkaConsumer
import pandas as pd
import json

consumer = KafkaConsumer(
    'stock-prices',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

data = []

print("Listening for stock prices...")

for msg in consumer:
    stock = msg.value
    print("Received:", stock)
    data.append(stock)

    # Keep only the last 100 messages
    if len(data) > 100:
        data.pop(0)

    # Save to CSV (optional)
    df = pd.DataFrame(data)
    df.to_csv('latest_stock_data.csv', index=False)
