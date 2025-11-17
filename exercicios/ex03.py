def ex03_read_csv(spark: SparkSession, input_path: str) -> DataFrame:
    """
    Lê CSV gerado no ex02 e retorna um DataFrame com as mesmas colunas.
    """

    df = spark.read.csv(
        input_path,    
        header=True,    
        inferSchema=True 
                         
    )
    
    return df