# Creditcardpipeline
This project builds a Predictive Analytics Pipeline for Credit Card Transactions using Google Cloud Platform (GCP). It detects fraudulent transactions and churn prediction while providing anomaly detection alerts using BigQuery ML, Cloud Dataflow, Cloud Functions, Cloud Run, and Looker Studio.
# Credit Card Transactions Predictive Analytics Pipeline (GCP)

This project builds a **Predictive Analytics Pipeline for Credit Card Transactions** on **Google Cloud Platform (GCP)**. It detects **fraudulent transactions**, predicts **customer churn**, and provides **real-time anomaly detection alerts**.

## **Tech Stack**
- Google Cloud Storage (GCS)
- Cloud Dataflow (Apache Beam)
- BigQuery & BigQuery ML
- Cloud Functions & Pub/Sub
- Cloud Run
- Looker Studio

## **Project Structure**
- **Data Ingestion:** Raw transactions stored in GCS.
- **Data Processing:** Cloud Dataflow cleans and transforms data.
- **Model Training:** BigQuery ML for fraud & churn prediction.
- **Anomaly Detection:** Cloud Functions and Pub/Sub for alerts.
- **Dashboard:** Looker Studio for data visualization.
