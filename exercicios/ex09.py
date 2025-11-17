from pyspark.sql import SparkSession

def ex09_insert_vendas(spark: SparkSession) -> None:
    """
    Insere registros na lab.db.vendas variando o ano.
    """

    spark.sql("""
        INSERT INTO lab.db.vendas VALUES
        (1, 'Notebook', 5000.00, 2023),
        (2, 'Mouse', 150.00, 2023),
        (3, 'Teclado', 300.00, 2024),
        (4, 'Monitor', 1200.00, 2024)
    """)