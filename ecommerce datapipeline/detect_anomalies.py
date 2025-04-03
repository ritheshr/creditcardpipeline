from flask import Flask, request
from google.cloud import bigquery, pubsub_v1
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def detect_anomalies():
    client = bigquery.Client()
    
    # Query to detect anomalies
    query = """
    SELECT timestamp, amount 
    FROM `your-gcp-project.Creditcardusage.transactions`
    WHERE amount > (SELECT AVG(amount) + 2 * STDDEV(amount) FROM `your-gcp-project.Creditcardusage.transactions`)
    """
    
    results = client.query(query).result()
    
    anomalies = [dict(row) for row in results]
    if anomalies:
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path('ecommerce-455605', 'creditcard-anomalies')
        publisher.publish(topic_path, json.dumps(anomalies).encode('utf-8'))

    return {"message": "Anomaly detection completed.", "anomalies": anomalies}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
