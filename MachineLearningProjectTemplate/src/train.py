import os
from sklearn.externals import joblib
from . import data
from . import features
from . import model


def train(data_filepath, model_filepath, model_type):
    """
    Trains a model on the data from data_filepath and saves the trained model to model_filepath.
    
    Parameters:
        - data_filepath (str): filepath to load the data from
        - model_filepath (str): filepath to save the trained model to
        - model_type (str): the type of model to train, e.g. 'linear_regression', 'random_forest'
    """
    # Load data
    df = data.load_data(data_filepath)
    # Perform feature engineering
    df = features.engineer_features(df)
    # Split the data into training and test sets
    X = df.drop(['target'], axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=42)
    # Train model
    trained_model = model.train_model(X_train, y_train, model_type)
    # Save model
    model.save_model(trained_model, model_filepath)
    print("Model saved to: ", model_filepath)
