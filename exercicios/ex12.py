from pyspark.sql import SparkSession

def ex12_create_df_table(spark: SparkSession) -> None:
    """
    Cria DataFrame e salva como lab.db.tabela_df via writeTo.
    """

    table_name = "lab.db.tabela_df"
    

    dados = [
        (1, "Dado A"),
        (2, "Dado B"),
        (3, "Dado C")
    ]
    colunas = ["id", "valor"]
    df = spark.createDataFrame(dados, colunas)
    
    df.writeTo(table_name).createOrReplace()