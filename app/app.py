from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total request count', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency', ['endpoint'])

@app.route('/')
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    with REQUEST_LATENCY.labels(endpoint='/').time():
        time.sleep(random.uniform(0.1, 0.5))
    return 'Hello from monitored app!'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/error')
def error():
    REQUEST_COUNT.labels(method='GET', endpoint='/error').inc()
    return 'Error endpoint', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
