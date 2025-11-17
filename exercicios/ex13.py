from pyspark.sql import SparkSession, DataFrame

def ex13_time_travel(spark: SparkSession, version: int) -> DataFrame:
    """
    Retorna SELECT * FROM lab.db.vendas VERSION AS OF {version}
    """
    
    table_name = "lab.db.vendas"
    
    query = f"SELECT * FROM {table_name} VERSION AS OF {version}"
    
    df_snapshot = spark.sql(query)
    
    return df_snapshot