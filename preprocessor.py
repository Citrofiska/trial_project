import pandas as pd

def preprocessor():
    # Load data
    data = pd.read_csv('data.csv')
    # Preprocess data
    data = data.drop(['Unnamed: 0'], axis=1)
    data = data.drop(['Unnamed: 0.1'], axis=1)
    data = data.drop(['Unnamed: 0.1.1'], axis=1)
    return data