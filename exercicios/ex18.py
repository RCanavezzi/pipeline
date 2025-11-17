from pyspark.sql import SparkSession

def ex18_merge_into(spark: SparkSession) -> None:
    """
    Executa MERGE INTO em lab.db.vendas atualizando valores.
    """
    
    # 1. Definir os dados de origem (staging/updates)

    dados_novos = [
        (4, 'Monitor', 1350.00, 2024),  
        (5, 'Headset', 450.00, 2024)    
    ]
    colunas = ["id", "produto", "valor", "ano"]
    df_source = spark.createDataFrame(dados_novos, colunas)
    
    # 2. Criar uma View temporária para usar no comando SQL
    df_source.createOrReplaceTempView("vendas_novos_dados")
    
    # 3. Executar o MERGE INTO
    spark.sql("""
        MERGE INTO lab.db.vendas AS t
        USING vendas_novos_dados AS s
        ON t.id = s.id  -- Condição de correspondência (join)
        
        -- Se o ID corresponder, atualiza o valor
        WHEN MATCHED THEN
            UPDATE SET t.valor = s.valor
        
        -- Se o ID não corresponder, insere o novo registo
        WHEN NOT MATCHED THEN
            INSERT (id, produto, valor, ano)
            VALUES (s.id, s.produto, s.valor, s.ano)
    """)