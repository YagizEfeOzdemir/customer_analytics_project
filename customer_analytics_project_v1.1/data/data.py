import pandas as pd
import sqlite3

df = pd.read_csv("german.data",sep=r'\s+',header=None)
df.columns = ["Status", "Duration", "CreditHistory", "Purpose", "CreditAmount",
              "Savings", "Employment", "InstallmentRate", "PersonalStatusSex",
              "OtherDebtors", "ResidenceSince", "Property", "Age", "OtherInstallmentPlans",
              "Housing", "ExistingCredits", "Job", "NumPeopleLiable", "Telephone", "ForeignWorker", "Target"]


conn = sqlite3.connect("german_data.db")

df.to_sql("german_data",conn,if_exists="replace",index=False)


conn.close()