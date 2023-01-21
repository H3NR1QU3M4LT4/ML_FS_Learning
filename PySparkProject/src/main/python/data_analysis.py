from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier


def analyze_data(data_df):
    # Convert categorical variables to numerical variables
    indexers = [
        StringIndexer(inputCol=column,
                      outputCol=column + "_index").fit(data_df)
        for column in categorical_columns
    ]
    data_df = Pipeline(stages=indexers).fit(data_df).transform(data_df)

    # Assemble the feature vectors
    assembler = VectorAssembler(
        inputCols=[column + "_index"
                   for column in categorical_columns] + numerical_columns,
        outputCol="features")
    data_df = assembler.transform(data_df)

    # Split the data into training and test sets
    training_df, test_df = data_df.randomSplit([0.7, 0.3])

    # Train a Random Forest Classifier
    classifier = RandomForestClassifier(labelCol="is_fraud",
                                        featuresCol="features")
    model = classifier.fit(training_df)

    # Use the model to make predictions on the test set
    predictions_df = model.transform(test_df)

    # Compute the accuracy of the model
    accuracy = predictions_df.filter(
        predictions_df.is_fraud ==
        predictions_df.prediction).count() / predictions_df.count()

    # Return the accuracy of the model
    return accuracy
