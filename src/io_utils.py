import pandas as pd

def load_data(path="../data/health_study_dataset.csv"):
    """
    Load data from CSV file and return as DataFrame
    """

    df = pd.read_csv(path)
    
    return df

def data_check(df):
    """
    Print first 5 rows and
    check data for: missing, duplicated, unique values
    """
    print("First 5 rows:")
    print(df.head())
    # print("\nSummary statistic:")
    # print(df.describe(include="all"))
    print("\nMissing values:")
    print (df.isna().sum())
    print("\nDuplicated values:")
    print(df.duplicated().sum())
    print("\nUnique values:")
    print(df["id"].nunique(), len(df))
