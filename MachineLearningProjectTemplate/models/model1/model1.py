import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def train_linear_regression(X_train, y_train):
    """
    Trains a linear regression model on the given training data.
    
    Parameters:
        - X_train (numpy.array): Training data for the independent variables
        - y_train (numpy.array): Training data for the dependent variable
        
    Returns:
        - sklearn.linear_model.LinearRegression: trained linear regression model
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_linear_regression(model, X_test, y_test):
    """
    Evaluates a linear regression model on the given test data.
    
    Parameters:
        - model (sklearn.linear_model.LinearRegression): trained linear regression model
        - X_test (numpy.array): Test data for the independent variables
        - y_test (numpy.array): Test data for the dependent variable
        
    Returns:
        - tuple: containing the following:
            - float: mean squared error
            - float: coefficient of determination (R^2)
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def save_linear_regression(model, filepath):
    """
    Saves a trained linear regression model to a specified file.
    
    Parameters:
        - model (sklearn.linear_model.LinearRegression): trained linear regression model
        - filepath (str): Filepath to save the model to
    """
    import joblib
    joblib.dump(model, filepath)


def load_linear_regression(filepath):
    """
    Loads a trained linear regression model from a specified file.
    
    Parameters:
        - filepath (str): Filepath to load the model from
        
    Returns:
        - sklearn.linear_model.LinearRegression: trained linear regression model
    """
    import joblib
    model = joblib.load(filepath)
    return model
