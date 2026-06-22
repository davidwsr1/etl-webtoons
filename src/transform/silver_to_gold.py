from pyspark.sql.functions import (
    desc,
    sum,
    count
)


def silver_to_gold(df_silver):

    # Ranking dos webtoons
    top_webtoons = (
        df_silver
        .orderBy(desc("likes"))
    )

    (
        top_webtoons.write
        .mode("overwrite")
        .parquet("data/gold/top_webtoons.parquet")
    )

    # Likes acumulados por gênero
    likes_por_genero = (
        df_silver
        .groupBy("genero")
        .agg(
            sum("likes").alias("likes_totais")
        )
        .orderBy(desc("likes_totais"))
    )

    (
        likes_por_genero.write
        .mode("overwrite")
        .parquet("data/gold/likes_por_genero.parquet")
    )

    # Quantidade de obras por gênero
    generos_populares = (
        df_silver
        .groupBy("genero")
        .agg(
            count("*").alias("quantidade")
        )
        .orderBy(desc("quantidade"))
    )

    (
        generos_populares.write
        .mode("overwrite")
        .parquet("data/gold/generos_populares.parquet")
    )

    print("Gold gerado com sucesso!")