import pandas as pd


def stem(name=None):
    df = pd.read_csv('main_endings.csv')
    print(df.head())
    if name is None:
        print('Hello, World!')
    else:
        print(f"Hello, {name}")
