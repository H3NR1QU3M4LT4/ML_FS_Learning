import pandas as pd
from pyspark.sql import SparkSession
from src.main.python.data_analysis import analyze_data


def test_analyze_data():
    # Create a SparkSession
    spark = SparkSession.builder.appName("MyProject").getOrCreate()

    # Create a test DataFrame
    data = {
        'transaction_id': [1, 2, 3, 4],
        'amount': ['100', '200', '300', '400'],
        'timestamp': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
        'is_fraud': ['1', '0', '0', '1']
    }
    test_df = spark.createDataFrame(pd.DataFrame(data))

    # Analyze the test DataFrame
    accuracy = analyze_data(test_df)

    # Assert that the accuracy of the model is above a certain threshold
    assert accuracy > 0.8
