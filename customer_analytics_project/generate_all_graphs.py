"""
This script loads the cleaned dataset and generates all visualizations
defined in reports/graphs/graphs.py. The resulting images are saved to
reports/images/.
"""

import pandas as pd
from reports.graphs.graphs import *

def main():
    df = pd.read_csv("data/german_cleaned.csv")

    plot_target_distribution(df)
    plot_purpose_vs_target(df)
    plot_credit_amount_vs_target(df)
    plot_correlation_heatmap(df)
    plot_duration_distribution(df)
    plot_credit_amount_distribution(df)
    plot_pairplot(df)
    plot_violinplot(df)
    plot_employment_vs_target(df)
    plot_purpose_vs_employment(df)
    plot_savings_vs_credit(df)
    plot_status_vs_target(df)

    print("All graphs generated and saved to reports/images/")

if __name__ == "__main__":
    main()
