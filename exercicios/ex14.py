from pyspark.sql import SparkSession

def ex14_export_vendas_csv(spark: SparkSession, path: str) -> None:
    """
    Salva lab.db.vendas como CSV no path.
    """

    table_name = "lab.db.vendas"

    df = spark.table(table_name)

    df.write.csv(
        path,
        header=True,
        mode="overwrite"
    )