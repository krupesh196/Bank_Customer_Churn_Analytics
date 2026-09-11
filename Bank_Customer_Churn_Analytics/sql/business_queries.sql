SELECT Country,COUNT(*) Customers,SUM(Churn) Churned,ROUND(100*AVG(Churn),2) ChurnRate FROM bank_customers GROUP BY Country ORDER BY ChurnRate DESC;
SELECT NumOfProducts,COUNT(*) Customers,ROUND(100*AVG(Churn),2) ChurnRate FROM bank_customers GROUP BY NumOfProducts;
SELECT IsActiveMember,ROUND(100*AVG(Churn),2) ChurnRate FROM bank_customers GROUP BY IsActiveMember;
