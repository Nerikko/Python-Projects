from pyspark.sql import DataFrame


def save_data(df: DataFrame, path: str, file_type: str = 'csv') -> None:
    if file_type == 'csv':
        df.write.csv(path, header=True)
    elif file_type == 'excel':
        df.write.format("com.crealytics.spark.excel") \
            .option("header", "true") \
            .save(path)
    else:
        raise ValueError("Unsupported file type. Use 'csv' or 'excel'.")

