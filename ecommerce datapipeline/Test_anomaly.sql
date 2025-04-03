SELECT *
FROM ML.PREDICT(
    MODEL `Creditcardusage.anomaly_detection_model`, 
    (
        SELECT 
            total_trans_amt, 
            total_trans_ct, 
            avg_utilization_ratio, 
            total_amt_chng_q4_q1, 
            total_ct_chng_q4_q1 
        FROM `ecommerce-455605.Creditcardusage.card`
        LIMIT 10
    )
);
