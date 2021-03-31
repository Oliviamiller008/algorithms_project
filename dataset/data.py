import pandas as pd


def load_data():
    dataset = pd.read_csv("dataset/exercise_dataset.csv")
    dataset.rename(columns={"Activity, Exercise or Sport (1 hour)": "Activity", "Calories per kg": "Calories_per_kg"}
                   , inplace=True)
    data_required = dataset[['Activity', 'Calories_per_kg']]
    data_required.set_index("Activity", inplace=True)
    data_required = data_required.apply(lambda x: x * 2.20462)  # convert to calories per pound
    data = data_required.to_dict()['Calories_per_kg']
    return data


if __name__ == '__main__':
    print(load_data())
