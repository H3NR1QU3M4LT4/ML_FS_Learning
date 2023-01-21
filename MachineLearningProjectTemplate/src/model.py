import os
from sklearn.externals import joblib


def save_model(model, filepath):
    """
    Saves a trained model to a specified filepath.
    
    Parameters:
        - model: trained model
        - filepath (str): filepath to save the model to
    """
    joblib.dump(model, filepath)


def load_model(filepath):
    """
    Loads a trained model from a specified filepath.
    
    Parameters:
        - filepath (str): filepath to load the model from
        
    Returns:
        - Trained model
    """
    return joblib.load(filepath)


def check_model_exists(filepath):
    """
    Check if the trained model already exists in the specified filepath.
    
    Parameters:
        - filepath (str): Filepath to check for the model
        
    Returns:
        - bool: True if the model already exists, False otherwise
    """
    return os.path.isfile(filepath)


def train_model(X_train, y_train, model_type):
    """
    Train a model of a specified type with X_train, y_train data.
    
    Parameters:
        - X_train (numpy.array): Training data for the independent variables
        - y_train (numpy.array): Training data for the dependent variable
        - model_type (str): the type of model to train, e.g. 'linear_regression', 'random_forest'
        
    Returns:
        - Trained model
    """
    if model_type == 'linear_regression':
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
    elif model_type == 'random_forest':
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor()
    else:
        raise ValueError(f"Invalid model type: {model_type}")
        model.fit(X_train, y_train)
        return model
