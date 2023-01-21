import os
import pandas as pd


def load_data(filepath):
    """
    Loads data from a specified filepath into a pandas DataFrame.
    
    Parameters:
        - filepath (str): Filepath to load the data from
        
    Returns:
        - pandas.DataFrame: DataFrame containing the loaded data
    """
    return pd.read_csv(filepath)


def save_data(df, filepath):
    """
    Saves data from a pandas DataFrame to a specified filepath.
    
    Parameters:
        - df (pandas.DataFrame): DataFrame containing the data to be saved
        - filepath (str): Filepath to save the data to
    """
    df.to_csv(filepath, index=False)


def check_data_exists(filepath):
    """
    Check if the data already exists in the specified filepath.
    
    Parameters:
        - filepath (str): Filepath to check for the data
        
    Returns:
        - bool: True if the data already exists, False otherwise
    """
    return os.path.isfile(filepath)


def download_data(url, filepath):
    """
    Download data from a specified URL and save it to a filepath.
    
    Parameters:
        - url (str): URL to download the data from
        - filepath (str): Filepath to save the downloaded data to
    """
    import urllib.request
    urllib.request.urlretrieve(url, filepath)
