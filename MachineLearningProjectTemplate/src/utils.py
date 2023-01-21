import pandas as pd
import numpy as np


def missing_values_table(df):
    """
    Returns a table of the number and percentage of missing values in each column of a pandas DataFrame.
    
    Parameters:
        - df (pandas.DataFrame): DataFrame to check for missing values
    
    Returns:
        - pandas.DataFrame: Table of missing values in each column of the input DataFrame
    """
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(columns={
        0: 'Missing Values',
        1: '% of Total Values'
    })
    return mis_val_table_ren_columns


def plot_correlation_matrix(df):
    """
    Plots a heatmap of the correlation matrix of a pandas DataFrame.
    
    Parameters:
        - df (pandas.DataFrame): DataFrame to plot the correlation matrix of
    """
    corr = df.corr()
    sns.heatmap(corr,
                xticklabels=corr.columns,
                yticklabels=corr.columns,
                cmap='coolwarm')
    plt.show()


def evaluate_model(model, X_test, y_test):
    """
    Evaluates a trained model using test data.
    
    Parameters:
        - model: trained model
        - X_test (numpy.array): test data for the independent variables
        - y_test (numpy.array): test data for the dependent variable
        
    Returns:
        - float: mean squared error of the model's predictions
        - float: coefficient of determination (R^2) of the model's predictions
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2
