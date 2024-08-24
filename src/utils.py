import pandas as pd

def load_data(filepath):
    """
    Loads data from a CSV file.
    """
    return pd.read_csv(filepath)

def save_results(data, filepath):
    """
    Saves the DataFrame to a CSV file.
    """
    data.to_csv(filepath, index=False)

def print_summary(data):
    """
    Prints a summary of the processed data.
    """
    print("Summary of Processed Data:")
    print(f"Total Entries: {len(data)}")
    print(f"Unique Moods: {data['mood'].nunique()}")
    print(data['mood'].value_counts())