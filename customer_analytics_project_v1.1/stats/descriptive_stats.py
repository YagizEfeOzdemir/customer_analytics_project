def descriptive_stats(df, column):
    from scipy import stats
    import numpy as np


    data = df[column]
    mean = float(data.mean())
    median = float(data.median())
    mode = int(data.mode()[0])
    min = int(data.mean())
    max = int(data.mean())
    std = float(data.std())
    var = float(data.var())
    iqr = float(stats.iqr(data))
    q1 = float(np.percentile(data, [25]))
    q3 = float(np.percentile(data, [75]))

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "std": std,
        "var": var,
        "iqr": iqr,
        "min": min, "max": max,
        "q1": q1, "q3": q3
        }
