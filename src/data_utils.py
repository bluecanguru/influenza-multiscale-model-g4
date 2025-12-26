#Exemplo

import pandas as pd

def load_features(path):
    """
    Load processed feature matrix.
    """
    return pd.read_csv(path)

def load_epidemiological_data(path):
    """
    Load aggregated epidemiological data.
    """
    return pd.read_csv(path)

def normalize_column(df, column):
    """
    Normalize a column between 0 and 1.
    """
    df[column] = (df[column] - df[column].min()) / (
        df[column].max() - df[column].min()
    )
    return df
