from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def remove_white_spaces(df: DataFrame) -> DataFrame:
    for column in df.columns:
        df = df.withColumn(column, F.regexp_replace(F.col(column), r'\s+', ' '))
        df = df.withColumn(column, F.trim(F.col(column)))
    return df