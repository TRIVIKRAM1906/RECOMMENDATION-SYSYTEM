import pandas as pd

def load_movielens_100k():
    path = "https://files.grouplens.org/datasets/movielens/ml-100k/u.data"
    df = pd.read_csv(path, sep='\t', names=['userId', 'movieId', 'rating', 'timestamp'])
    return df
