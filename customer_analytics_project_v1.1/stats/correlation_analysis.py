

def correlation_analysis(df, col1, col2):
    pearson = float(df[[col1, col2]].corr(method='pearson').iloc[0, 1])
    spearman = float(df[[col1, col2]].corr(method='spearman').iloc[0, 1])
    return {"pearson_correlation": pearson, "spearman_correlation": spearman}
