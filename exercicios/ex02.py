from pyspark.sql import SparkSession, DataFrame

def ex02_save_csv(spark: SparkSession, output_path: str) -> None:
    """
    Cria um DataFrame e salva em CSV em output_path.
    Deve gerar header.
    """

    print(f"A criar DataFrame de exemplo...")
    dados = [
        (10, "Produto A", 19.99),
        (20, "Produto B", 200.50),
        (30, "Produto C", 0.89)
    ]
    colunas = ["id_produto", "nome", "preco"]
    df = spark.createDataFrame(dados, colunas)

    print(f"A guardar DataFrame em CSV no caminho: {output_path}")
    
    df.write.csv(
        output_path,      
        header=True,      
        mode="overwrite" 
                          
    )
    
    print("Ficheiro CSV guardado com sucesso!")