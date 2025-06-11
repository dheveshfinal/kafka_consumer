from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

stocks = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']

print("Producing stock prices...")

while True:
    stock_data = {
        'ticker': random.choice(stocks),
        'price': round(random.uniform(100, 1500), 2),
        'volume': random.randint(1000, 10000),
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }

    producer.send('stock-prices', value=stock_data)
    print("Sent:", stock_data)
    time.sleep(1)
