""" This file contains visualization functions.
The functions take a DataFrame (df) as input and save the resulting plots to the reports/images/ directory. """

import seaborn as sns
from matplotlib import pyplot as plt

sns.set(style="whitegrid")

def plot_target_distribution(df):
    plt.figure(figsize=(6,6))
    df['Target'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightblue', 'salmon'], startangle=90)
    plt.title('Target Variable Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('reports/images/target_distribution.png')
    plt.close()

def plot_purpose_vs_target(df):
    plt.figure(figsize=(12,6))
    sns.countplot(x='Purpose', hue='Target', data=df)
    plt.title('Loan Purpose vs. Target')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('reports/images/purpose_vs_target.png')
    plt.close()

def plot_credit_amount_vs_target(df):
    plt.figure(figsize=(8,6))
    sns.boxplot(x='Target', y='CreditAmount', data=df)
    plt.title('Credit Amount vs. Target')
    plt.tight_layout()
    plt.savefig('reports/images/credit_amount_vs_target.png')
    plt.close()

def plot_correlation_heatmap(df):
    plt.figure(figsize=(10,8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('reports/images/correlation_heatmap.png')
    plt.close()

def plot_duration_distribution(df):
    plt.figure(figsize=(8,6))
    sns.histplot(df['Duration'], kde=True, bins=30, color='skyblue')
    plt.title('Duration Distribution')
    plt.tight_layout()
    plt.savefig('reports/images/duration_distribution.png')
    plt.close()

def plot_credit_amount_distribution(df):
    plt.figure(figsize=(8,6))
    sns.histplot(df['CreditAmount'], kde=True, bins=30, color='green')
    plt.title('Credit Amount Distribution')
    plt.tight_layout()
    plt.savefig('reports/images/credit_amount_distribution.png')
    plt.close()

def plot_pairplot(df):
    sns.pairplot(df[['Age', 'CreditAmount', 'Duration', 'Target']], hue='Target')
    plt.savefig('reports/images/pairplot.png')
    plt.close()

def plot_violinplot(df):
    plt.figure(figsize=(8,6))
    sns.violinplot(x='Target', y='Duration', data=df)
    plt.title('Duration Distribution by Target')
    plt.tight_layout()
    plt.savefig('reports/images/violinplot.png')
    plt.close()

def plot_employment_vs_target(df):
    plt.figure(figsize=(10,6))
    sns.countplot(x='Employment', hue='Target', data=df)
    plt.title('Employment Duration vs. Target')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('reports/images/employment_vs_target.png')
    plt.close()

def plot_purpose_vs_employment(df):
    plt.figure(figsize=(12,6))
    sns.countplot(x='Purpose', hue='Employment', data=df)
    plt.title('Loan Purpose vs. Employment Duration')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('reports/images/purpose_vs_employment.png')
    plt.close()

def plot_savings_vs_credit(df):
    plt.figure(figsize=(10,6))
    sns.boxplot(x='Savings', y='CreditAmount', data=df)
    plt.title('Savings Account vs. Credit Amount')
    plt.tight_layout()
    plt.savefig('reports/images/savings_vs_credit.png')
    plt.close()

def plot_status_vs_target(df):
    plt.figure(figsize=(10,6))
    sns.countplot(x='PersonalStatusSex', hue='Target', data=df)
    plt.title('Personal Status vs. Target')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('reports/images/status_vs_target.png')
    plt.close()
