from pyspark.sql import SparkSession

def ex15_create_parquet_table(spark: SparkSession, path: str) -> None:
    """
    Cria um DataFrame simples e salva como Parquet.
    """

    dados = [
        ("Parquet", 1, True),
        ("CSV", 2, False),
        ("JSON", 3, False)
    ]
    colunas = ["formato", "id", "comprimido"]
    df = spark.createDataFrame(dados, colunas)
    
    df.write.parquet(
        path,
        mode="overwrite"
    )