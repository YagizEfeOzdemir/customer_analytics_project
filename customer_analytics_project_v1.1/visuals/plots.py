

def creditamount_duration_pearson(df):
    #1.2
    from scipy.stats import pearsonr
    import matplotlib.pyplot as plt

    x = df["CreditAmount"]
    y = df["Duration"]

    r, p = pearsonr(x, y)

    plt.scatter(x, y,alpha=1,edgecolors="black",color="blue")
    plt.title("CreditAmount vs Duration")
    plt.xlabel("CreditAmount")
    plt.ylabel("Duration")
    plt.show()

    print(f"Pearson r = {r:.2f}, p-val = {p:.5f}")

def age_savings_spearman(df):
    #2.2
    from scipy.stats import spearmanr
    import matplotlib.pyplot as plt

    x = df['Age']
    y = df['Savings']

    r, p = spearmanr(x,y)

    plt.scatter(x,y,alpha=1,edgecolors="black",color="yellow")
    plt.title("Age vs Savings")
    plt.xlabel("Age")
    plt.ylabel("Savings")
    plt.show()

    print(f"Spearman r = {r:.2f}, p-val = {p:.5f}")

def installmentrate_creditamount_spearman(df):
    #3.2
    from scipy.stats import spearmanr
    import matplotlib.pyplot as plt


    x = df['InstallmentRate']
    y = df['CreditAmount']

    r, p = spearmanr(x, y)

    plt.scatter(x, y, alpha=1, edgecolors="black", color="Red")
    plt.title("InstallmentRate vs CreditAmount")
    plt.xlabel("InstallmentRate")
    plt.ylabel("CreditAmount")
    plt.show()

    print(f"spearmanr r = {r:.2f}, p-val = {p:.5f}")

def purpose_credit_history_chi2(df):
    #4.2
    from scipy import stats
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    x = df['Purpose']
    y = df['CreditHistory']

    table = pd.crosstab(x,y)
    chi2 , p , dof ,expected =stats.chi2_contingency(table)

    sns.heatmap(table, annot=True, fmt='d', cmap='YlGnBu')
    plt.title("Purpose vs CreditHistory - Heatmap", fontsize=14)
    plt.ylabel("Purpose")
    plt.xlabel("CreditHistory")
    plt.xticks(rotation=75)
    plt.show()

    print(f"chi2 = {chi2:.2f}, p-val = {p:.5f},dof = {dof}")

def target_duration_ztest(df):
    #5.2
    from statsmodels.stats.weightstats import ztest
    import seaborn as sns
    import matplotlib.pyplot as plt

    duration_good = df[df['Target'] == 1]['Duration']
    duration_bad  = df[df['Target'] == 2]['Duration']

    z , p  = ztest(duration_good,duration_bad)

    sns.barplot(x='Target',y='Duration',data = df,width=0.5,errorbar='sd')
    plt.title("Target vs Duration")
    plt.xlabel("Target")
    plt.ylabel("Duration")
    plt.show()

    print(f"z score: {z:.4f} p value: {p:.5f}")

def target_credit_amount_ttest(df):
    #6.2
    from scipy import stats
    import matplotlib.pyplot as plt
    import seaborn as sns

    good_amount = df[df['Target'] == 1]['CreditAmount']
    bad_amount = df[df['Target'] == 2]['CreditAmount']

    t , p = stats.ttest_ind(good_amount,bad_amount)

    sns.barplot(data=df,x="Target",y='CreditAmount',width=0.5,errorbar='sd',color="red")
    plt.title("Target vs CreditAmount")
    plt.xlabel("Target")
    plt.ylabel("CreditAmount")
    plt.show()

    print(f"t score: {t:.4f}  p val: {p:.5f}")



def credit_amount_outlier_test(df):
#7.2
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    Q1,Q3 = np.percentile(df['CreditAmount'],[25,75])

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR


    outliers = df[(df["CreditAmount"] < lower_bound) | (df["CreditAmount"] > upper_bound)]

    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("lower bound:", lower_bound)
    print("upper bound:", upper_bound)
    print("\nOutliers:")
    print(outliers['CreditAmount'])

    sns.boxplot(x=df['CreditAmount'],color='red')
    plt.title("Summary of Credit Amount")
    plt.show()