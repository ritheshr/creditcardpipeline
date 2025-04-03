Credit Card Transactions Predictive Analytics Pipeline on GCP

#📌 Overview

This project builds a Predictive Analytics Pipeline for Credit Card Transactions on Google Cloud Platform (GCP). The system detects fraudulent transactions, performs churn prediction, and enables anomaly detection alerts using BigQuery ML, Cloud Dataflow, Cloud Functions, Cloud Run, and Looker Studio.

#📂 Architecture

Google Cloud Storage (GCS) – Stores raw transaction data.

Cloud Dataflow (Apache Beam) – Processes and cleans transaction data.

BigQuery & BigQuery ML – Trains fraud detection and churn prediction models.

Cloud Functions & Cloud Pub/Sub – Handles real-time anomaly detection and alerting.

Cloud Run – Deploys predictive APIs.

Looker Studio – Visualizes transaction insights.

#🚀 Implementation Steps

1️⃣ Setup GCP Environment

Create a new GCP Project via Google Cloud Console.

Enable APIs: Cloud Storage, Dataflow, BigQuery, Cloud Functions, Cloud Run, Looker Studio.

Set IAM permissions for service accounts.

2️⃣ Store Raw Data in Cloud Storage

Download the dataset from Kaggle.

Upload to Cloud Storage: dataset in folders

#Data Preprocessing with Cloud Dataflow

Create a Dataflow pipeline to clean and transform data.

Python script for Apache Beam:
