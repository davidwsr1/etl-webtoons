from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.extract.extrair_webtoon import extrair_webtoons
from src.load.load import salvar_bronze_csv
from src.spark.criar_spark import criar_spark
from src.transform.bronze_to_silver import bronze_to_silver
from src.transform.silver_to_gold import silver_to_gold


def executar_pipeline():

    dados = extrair_webtoons()

    salvar_bronze_csv(dados)

    spark = criar_spark()

    df_silver = bronze_to_silver(spark)

    silver_to_gold(df_silver)

    spark.stop()


with DAG(
    dag_id="webtoon_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["spark", "etl", "webtoon"],
) as dag:

    pipeline = PythonOperator(
        task_id="executar_pipeline",
        python_callable=executar_pipeline,
    )

    pipeline