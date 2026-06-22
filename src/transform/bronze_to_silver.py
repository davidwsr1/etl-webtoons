from pyspark.sql.functions import (
    col,
    regexp_replace,
    when,
    current_date,
    trim,
    initcap
)


def bronze_to_silver(spark):
    """
    Lê os dados da camada Bronze,
    realiza limpeza e padronização,
    e salva na camada Silver.
    """

    # Leitura do Bronze
    df = (
        spark.read
        .option("header", True)
        .csv("data/bronze/webtoons.csv")
    )

    # Limpeza básica
    df = (
        df
        .withColumn("titulo", trim(col("titulo")))
        .withColumn("genero", initcap(trim(col("genero"))))
        .withColumn("likes", trim(col("likes")))
    )

    # Remove separadores de milhar
    df = df.withColumn(
        "likes",
        regexp_replace(col("likes"), ",", "")
    )

    # Conversão de likes
    df = (
        df.withColumn(
            "likes",
            when(
                col("likes").endswith("M"),
                regexp_replace(col("likes"), "M", "").cast("double") * 1000000
            )
            .when(
                col("likes").endswith("K"),
                regexp_replace(col("likes"), "K", "").cast("double") * 1000
            )
            .otherwise(
                col("likes").cast("double")
            )
        )
    )

    # Converte para inteiro
    df = df.withColumn(
        "likes",
        col("likes").cast("long")
    )

    # Remove registros duplicados
    df = df.dropDuplicates()

    # Remove linhas inválidas
    df = df.dropna(
        subset=[
            "titulo",
            "genero",
            "likes"
        ]
    )

    # Adiciona metadata de processamento
    df = df.withColumn(
        "data_processamento",
        current_date()
    )

    print("\nPrévia da camada Silver:")
    df.show(10, truncate=False)

    # Salva em Parquet
    (
        df.write
        .mode("overwrite")
        .parquet("data/silver/webtoons_clean.parquet")
    )

    print("Silver gerado com sucesso!")

    return df