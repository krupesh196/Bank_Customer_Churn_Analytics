import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("../data/bank_customers.csv")
print("Churn Rate:",round(df.Churn.mean()*100,2),"%")
print(df.groupby("Country").Churn.mean().mul(100).round(2))
print(df.groupby("NumOfProducts").Churn.mean().mul(100).round(2))
df.groupby("Country").Churn.mean().mul(100).plot(kind="bar",title="Churn Rate by Country")
plt.ylabel("Churn %"); plt.tight_layout(); plt.savefig("churn_by_country.png",dpi=150); plt.show()
