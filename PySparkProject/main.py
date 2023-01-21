from pyspark.sql import SparkSession
from src.main.python.data_processing import clean_data, transform_data
from src.main.python.data_analysis import analyze_data


def main():
    # Create a SparkSession
    spark = SparkSession.builder.appName("PySparkProject").getOrCreate()

    # Load the data into a DataFrame
    file_path = "/src/main/resources/data/creditcard.csv"
    data_df = spark.read.format("csv").option("header", "True").load(file_path)

    # Perform data processing and analysis
    cleaned_df = clean_data(data_df)
    transformed_df = transform_data(cleaned_df)
    result_df = analyze_data(transformed_df)

    # Save the results to a file or a database
    result_df.write.format("csv").save("/src/main/resources/data/results.csv")


if __name__ == "__main__":
    main()
