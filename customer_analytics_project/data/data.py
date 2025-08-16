"""
Reads the original raw data file (german.data),
assigns column names, and saves it as a clean CSV (german.csv)
for further processing.
"""

import pandas as pd

df = pd.read_csv("german.data",sep=r'\s+',header=None)

df.columns = ["Status", "Duration", "CreditHistory", "Purpose", "CreditAmount",
              "Savings", "Employment", "InstallmentRate", "PersonalStatusSex",
              "OtherDebtors", "ResidenceSince", "Property", "Age", "OtherInstallmentPlans",
              "Housing", "ExistingCredits", "Job", "NumPeopleLiable", "Telephone", "ForeignWorker", "Target"]

df.to_csv("german.csv",index=False)