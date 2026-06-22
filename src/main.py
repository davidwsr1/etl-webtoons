from extract.extrair_webtoon import extrair_webtoons
from load.load import salvar_bronze_csv

from spark.criar_spark import criar_spark

from transform.bronze_to_silver import bronze_to_silver
from transform.silver_to_gold import silver_to_gold


def main():

    print("Iniciando pipeline...")

    # Extract
    dados = extrair_webtoons()

    # Bronze
    salvar_bronze_csv(dados)

    # Spark
    spark = criar_spark()

    # Silver
    df_silver = bronze_to_silver(spark)

    # Gold
    silver_to_gold(df_silver)

    spark.stop()

    print("Pipeline concluída com sucesso!")


if __name__ == "__main__":
    main()