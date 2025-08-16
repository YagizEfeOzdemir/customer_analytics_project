from scipy import stats
import numpy as np

def detect_outliers_iqr(series):
    iqr = stats.iqr(series)
    q1, q3 = np.percentile(series, [25, 75])
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = []
    for i in series:
        if i < lower or i > upper:
            outliers.append(i)
    return {"outliers" : outliers}
