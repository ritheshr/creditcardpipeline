SELECT *
FROM ML.PREDICT(
  MODEL `ecommerce-455605.Creditcardusage.churn_prediction`, 
  (
    SELECT 
        customer_age, 
        dependent_count, 
        education_level, 
        marital_status, 
        income_category, 
        card_category, 
        months_on_book, 
        total_relationship_count, 
        months_inactive_12_mon, 
        contacts_count_12_mon, 
        credit_limit, 
        total_revolving_bal, 
        avg_open_to_buy, 
        total_amt_chng_q4_q1, 
        total_trans_amt, 
        total_trans_ct, 
        total_ct_chng_q4_q1, 
        avg_utilization_ratio
    FROM `ecommerce-455605.Creditcardusage.card`
    LIMIT 10
  )
);
