from pyspark.sql import SparkSession

def ex17_delete_and_vacuum(spark: SparkSession) -> None:
    """
    Deleta linhas por condição e roda:
    CALL lab.system.expire_snapshots(...)
    """

    table_name = "lab.db.vendas"
    

    spark.sql(f"DELETE FROM {table_name} WHERE ano = 2023")
    

    spark.sql(f"""
        CALL lab.system.expire_snapshots(
            table => '{table_name}',
            older_than => NOW(),
            retain_last => 1
        )
    """)