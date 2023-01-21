import os
from src import data, features, model, train, utils

# Define filepaths
data_filepath = 'data/raw_data.csv'
processed_data_filepath = 'data/processed_data.csv'
model_filepath = 'models/trained_model.pkl'


def main():
    # Check if data needs to be downloaded
    if not data.check_data_exists(data_filepath):
        data.download_data('https://example.com/data.csv', data_filepath)

    # Check if processed data already exists
    if not data.check_data_exists(processed_data_filepath):
        # Load data
        df = data.load_data(data_filepath)
        # Perform feature engineering
        df = features.engineer_features(df)
        # Save processed data
        data.save_data(df, processed_data_filepath)
    else:
        # Load processed data
        df = data.load_data(processed_data_filepath)

    # Split the data into training and test sets
    X = df.drop(['target'], axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=42)

    # Check if model already exists
    if not model.check_model_exists(model_filepath):
        # Train model
        trained_model = model.train_model(X_train, y_train, 'random_forest')
        # Save model
        model.save_model(trained_model, model_filepath)
    else:
        # Load trained model
        trained_model = model.load_model(model_filepath)

    # Evaluate model on test data
    mse, r2 = utils.evaluate_model(trained_model, X_test, y_test)
    print("Mean Squared Error: ", mse)
    print("R^2: ", r2)


if __name__ == '__main__':
    main()
