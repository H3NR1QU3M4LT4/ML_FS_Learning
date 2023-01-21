import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def train_logistic_regression(X_train, y_train):
    """
    Trains a logistic regression model on the given training data.
    
    Parameters:
        - X_train (numpy.array): Training data for the independent variables
        - y_train (numpy.array): Training data for the dependent variable
        
    Returns:
        - sklearn.linear_model.LogisticRegression: trained logistic regression model
    """
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_logistic_regression(model, X_test, y_test):
    """
    Evaluates a logistic regression model on the given test data.
    
    Parameters:
        - model (sklearn.linear_model.LogisticRegression): trained logistic regression model
        - X_test (numpy.array): Test data for the independent variables
        - y_test (numpy.array): Test data for the dependent variable
        
    Returns:
        - tuple: containing the following:
            - float: accuracy score
            - float: f1 score
            - numpy.array: confusion matrix
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
