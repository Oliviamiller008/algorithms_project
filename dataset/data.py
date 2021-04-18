import pandas as pd


def load_data():
    dataset = pd.read_csv("dataset/exercise_dataset_cleaned.csv")
    dataset.set_index("Exercise", inplace=True)
    data = dataset.T.to_dict('list')
    return data



