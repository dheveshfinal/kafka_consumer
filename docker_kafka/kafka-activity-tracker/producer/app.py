from flask import Flask, request, render_template
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    producer.send('user_events', data)
    return {'status': 'sent'}

if __name__ == '__main__':
    app.run(debug=True)
