from stats.descriptive_stats import descriptive_stats
from stats.hypothesis_tests import t_test
from stats.hypothesis_tests import z_test
from stats.hypothesis_tests import chi2_test
from stats.correlation_analysis import correlation_analysis
from stats.utils import detect_outliers_iqr
import sqlite3
import pandas as pd

conn = sqlite3.connect("../data/german_data.db")
df = pd.read_sql_query("SELECT * FROM german_cleaned",conn)

print(descriptive_stats(df, "CreditAmount"))
print(t_test(df, "CreditAmount",'Target'))
print(correlation_analysis(df, "CreditAmount", "Duration"))
print(detect_outliers_iqr(df["CreditAmount"]))
print(z_test(df,'CreditAmount','Target'))
print(chi2_test(df,"Age","Employment"))