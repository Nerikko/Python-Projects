from pyspark.sql import DataFrame


def load_data(spark, path: str, file_type: str = 'csv') -> DataFrame:
    if file_type == 'csv':
        df = spark.read.csv(path, header=True, inferSchema=True)
    elif file_type == 'excel':
        df = spark.read.format("com.crealytics.spark.excel") \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .load(path)
    else:
        raise ValueError("Unsupported file type. Use 'csv' or 'excel'.")
    return df
