from pyspark.sql import SparkSession


def criar_spark():
    return (
        SparkSession.builder
        .appName("ETL Webtoons")
        .getOrCreate()
    )