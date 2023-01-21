import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder


def create_polynomial_features(df, feature, degree):
    """
    Creates polynomial features of a given degree for a specified feature.
    
    Parameters:
        - df (pandas.DataFrame): Dataframe containing the feature
        - feature (str): Name of the feature to create polynomial features for
        - degree (int): Degree of the polynomial
        
    Returns:
        - pandas.DataFrame: Dataframe with the new polynomial features
    """
    for i in range(2, degree + 1):
        col_name = feature + f'_{i}'
        df[col_name] = df[feature]**i
    return df


def create_log_features(df, features):
    """
    Creates logarithmic features for specified features.
    
    Parameters:
        - df (pandas.DataFrame): Dataframe containing the features
        - features (list): List of feature names to create logarithmic features for
        
    Returns:
        - pandas.DataFrame: Dataframe with the new logarithmic features
    """
    for feature in features:
        col_name = 'log_' + feature
        df[col_name] = np.log1p(df[feature])
    return df


def create_interaction_features(df, features):
    """
    Creates interaction features for specified features.
    
    Parameters:
        - df (pandas.DataFrame): Dataframe containing the features
        - features (list): List of feature names to create interaction features for
        
    Returns:
        - pandas.DataFrame: Dataframe with the new interaction features
    """
    for i in range(len(features)):
        for j in range(i + 1, len(features)):
            col_name = features[i] + '_' + features[j]
            df[col_name] = df[features[i]] * df[features[j]]
    return df


def normalize_features(df, features):
    """
    Normalizes specified features using MinMaxScaler.
    
    Parameters:
        - df (pandas.DataFrame): Dataframe containing the features
        - features (list): List of feature names to normalize
        
    Returns:
        - pandas.DataFrame: Dataframe with the normalized features
    """
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])
    return df


def one_hot_encode_features(df, features):
    """
    One-hot encodes specified categorical features.
    
    Parameters:
        - df (pandas.DataFrame): Dataframe containing the features
        - features (list): List of feature names to one-hot encode
        
    Returns:
        - pandas.DataFrame: Dataframe with the one-hot encoded features
    """
    ohe = OneHotEncoder(sparse=False)
    for feature in features:
        one_hot_encoded_array = ohe.fit_transform(df[[feature]])
    one_hot_encoded_df = pd.DataFrame(
        one_hot_encoded_array,
        columns=[feature + '_' + str(i) for i in ohe.categories_[0]])
    df = pd.concat([df, one_hot_encoded_df], axis=1)
    df.drop([feature], axis=1, inplace=True)
    return df


# Import the necessary libraries
import pandas as pd

# Load the original data into a dataframe
df = pd.read_csv('data/processed/original_data.csv')

# Apply feature engineering techniques
df = create_polynomial_features(df, 'feature1', 3)
df = create_log_features(df, ['feature2', 'feature3'])
df = create_interaction_features(df, ['feature1', 'feature2', 'feature3'])
df = normalize_features(df, ['feature4', 'feature5'])
df = one_hot_encode_features(df, ['feature6'])

# Save the processed dataframe to a CSV file
df.to_csv('features/features.csv', index=False)