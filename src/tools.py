import pandas as pd

def basic_eda(df):
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing": df.isnull().sum().to_dict(),
        "describe": df.describe(include='all').to_dict()
    }
