"""
This script reads the raw CSV file, applies predefined mappings to
categorical columns, and outputs a cleaned version of the dataset.
"""
import pandas as pd
import mappings

df=pd.read_csv("../data/german.csv")
df.info()
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype("string")
df.info()


def map_categorical_columns(df):
    df['Status']=df['Status'].map(mappings.Status_Mapping)
    df['CreditHistory']=df['CreditHistory'].map(mappings.CreditHistory_Mapping)
    df['Purpose']=df['Purpose'].map(mappings.Purpose_Mapping)
    df['Savings']=df['Savings'].map(mappings.Savings_Mapping)
    df['Employment']=df['Employment'].map(mappings.Employment_Mapping)
    df['PersonalStatusSex']=df['PersonalStatusSex'].map(mappings.PersonalStatusSex_Mapping)
    df['OtherDebtors']=df['OtherDebtors'].map(mappings.OtherDebtors_Mapping)
    df['Property']=df['Property'].map(mappings.Property_Mapping)
    df['OtherInstallmentPlans']=df['OtherInstallmentPlans'].map(mappings.OtherInstallmentPlans_Mapping)
    df['Housing']=df['Housing'].map(mappings.Housing_Mapping)
    df['Job']=df['Job'].map(mappings.Job_Mapping)
    df['Telephone']=df['Telephone'].map(mappings.Telephone_Mapping)
    df['ForeignWorker']=df['ForeignWorker'].map(mappings.ForeignWorker_Mapping)
    return df

cleaned_df = map_categorical_columns(df)
cleaned_df.to_csv("../data/german_cleaned.csv", index=False)


"""No NaN check after or before mapping because the dataset contains no missing or unexpected categorical values.
 All possible category values are covered by the mapping dictionaries."""


























