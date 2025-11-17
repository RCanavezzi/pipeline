from pyspark.sql import SparkSession

TABLE = "lab.db.pessoas"

def ex05_insert_and_count(spark: SparkSession) -> int:
    """
    Faz INSERT de 3 linhas na tabela lab.db.pessoas e retorna a contagem (int).
    """

    spark.sql(f"""
        INSERT INTO {TABLE} VALUES
        (1, 'Ana'),
        (2, 'Bruno'),
        (3, 'Carla')
    """)

    count_df = spark.sql(f"SELECT COUNT(*) FROM {TABLE}")
    
    total_linhas = count_df.first()[0]
    
    return total_linhas