import pandas as pd
from pyspark.sql import SparkSession
from src.main.python.data_processing import clean_data, transform_data


def test_clean_data():
    # Create a SparkSession
    spark = SparkSession.builder.appName("MyProject").getOrCreate()

    # Create a test DataFrame
    data = {'column1': ['value1', 'value2', 'value3', None],
            'column2': ['value4', 'value5', None, None],
            'column3': ['value6', None, 'value7', 'value8']}
    test_df = spark.createDataFrame(pd.DataFrame(data))

    # Clean the test DataFrame
    cleaned_df = clean_data(test_df)

    # Assert that the cleaned DataFrame contains no missing values
    assert cleaned_df.na.drop().count() == cleaned_df.count()


def test_transform_data():
    # Create a SparkSession
    spark = SparkSession.builder.appName("MyProject").getOrCreate()

    # Create a test DataFrame
    data = {'transaction_id': [1, 2, 3, 4],
            'amount': ['100', '200', '300', '400'],
            'timestamp': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
            'is_fraud': ['1', '0', '0', '1']}
    test_df = spark.createDataFrame(pd.DataFrame(data))

    # Transform the test DataFrame
    transformed_df = transform_data(test_df)

    # Assert that the transformed DataFrame has the correct data types
    assert transformed_df.select('transaction_id').dtypes[0][1] == 'int'
    assert transformed_df.select('amount').dtypes[0][1] == 'float'
    assert transformed_df.select('timestamp').dtypes[0][1] == 'timestamp'
    assert transformed_df.select('is_fraud').dtypes[0][1] == 'int'
