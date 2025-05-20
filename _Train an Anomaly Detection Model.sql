CREATE OR REPLACE MODEL `ecommerce-455605.Creditcardusage.anomaly_detection_model`
OPTIONS(model_type='KMEANS', num_clusters=2)
AS
SELECT 
    total_trans_amt, 
    total_trans_ct, 
    avg_utilization_ratio,
    total_amt_chng_q4_q1, 
    total_ct_chng_q4_q1 
FROM `ecommerce-455605.Creditcardusage.card`;
