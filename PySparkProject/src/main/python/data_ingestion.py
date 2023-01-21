from pyspark import SparkContext
from pyspark.sql import SparkSession


def load_data(file_path: str):
    # Create a SparkSession
    spark = SparkSession.builder.appName("FraudDetection").getOrCreate()

    # Load the data into a DataFrame
    data_df = spark.read.format("csv").option("header", "True").load(file_path)

    # Return the DataFrame
    return data_df


if __name__ == "__main__":
    # Set the file path
    file_path = "path/to/transactions.csv"

    # Load the data
    data_df = load_data(file_path)

    # Print the DataFrame to check the data
    data_df.show()
