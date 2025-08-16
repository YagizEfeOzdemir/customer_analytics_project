from scipy import stats
from statsmodels.stats.weightstats import ztest
import pandas as pd

def z_test(df, column, target_col):
    group1 = df[df[target_col] == 1][column].astype(float)
    group2 = df[df[target_col] == 2][column].astype(float)
    z,p = ztest(group1,group2)
    z = float(z)
    p = float(p)
    mean1 = float(group1.mean())
    mean2 = float(group2.mean())
    return {"z_stat": z,"p_val": p,"mean1": mean1,"mean2": mean2}

def t_test(df, column, target_col):
    group1 = df[df[target_col] == 1][column]
    group2 = df[df[target_col] == 2][column]
    t, p = stats.ttest_ind(group1, group2, equal_var=False)
    t = float(t)
    p = float(p)
    mean1 = float(group1.mean())
    mean2 = float(group2.mean())
    return {"t_stat": t, "p_val": p, "mean1": mean1, "mean2": mean2}


def chi2_test(df, col1, col2):
    table = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = stats.chi2_contingency(table)
    chi2 =float(chi2)
    p = float(p)
    dof = int(dof)
    return {"chi2": chi2, "p_val": p, "dof": dof}