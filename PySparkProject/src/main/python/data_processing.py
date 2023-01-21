from pyspark.sql.functions import col, when


def clean_data(data_df):
    # Remove duplicates
    data_df = data_df.dropDuplicates()

    # Replace missing values with None
    data_df = data_df.na.fill("None")

    # Remove columns that have a high percentage of missing values
    data_df = data_df.dropna(thresh=int(data_df.count() * 0.6),
                             subset=data_df.columns)

    # Return the cleaned DataFrame
    return data_df


def transform_data(data_df):
    # Convert columns to the appropriate data types
    data_df = data_df.withColumn("transaction_id",
                                 col("transaction_id").cast("integer"))
    data_df = data_df.withColumn("amount", col("amount").cast("float"))
    data_df = data_df.withColumn("timestamp",
                                 col("timestamp").cast("timestamp"))
    data_df = data_df.withColumn(
        "is_fraud",
        when(col("is_fraud") == "1", True).otherwise(False))

    # Perform any additional transformation operations here

    # Return the transformed DataFrame
    return data_df


if __name__ == "__main__":
    # Create a SparkSession
    spark = SparkSession.builder.appName("DataProcessing").getOrCreate()

    # Load the data into a DataFrame
    file_path = "path/to/transactions.csv"
    data_df = spark.read.format("csv").option("header", "True").load(file_path)

    # Clean the data
    cleaned_df = clean_data(data_df)

    # Transform the data
    transformed_df = transform_data(cleaned_df)

    # Print the transformed DataFrame to check the data
    transformed_df.show()
