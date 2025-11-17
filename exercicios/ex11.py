from pyspark.sql import SparkSession

def ex11_history_and_detail(spark: SparkSession) -> dict:
    """
    Retorna dicionário: {"history": df_history.count(), "detail": df_detail.collect()}
    """
    
    table_name = "lab.db.vendas"
    

    df_history = spark.sql(f"SELECT * FROM {table_name}.history")
    

    df_detail = spark.sql(f"SELECT * FROM {table_name}.files")

    resultado = {
        "history": df_history.count(),
        "detail": df_detail.collect()
    }
    
    return resultado