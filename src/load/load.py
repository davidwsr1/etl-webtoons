import pandas as pd
import sqlite3


def salvar_bronze_csv(dados):
    df = pd.DataFrame(dados)

    df.to_csv(
        "data/bronze/webtoons.csv",
        index=False,
        encoding="utf-8"
    )

    print("Bronze CSV salvo com sucesso!")


def salvar_bronze_sqlite(dados):
    conn = sqlite3.connect(
        "data/bronze/webtoons.db"
    )

    df = pd.DataFrame(dados)

    df.to_sql(
        "webtoons",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Bronze SQLite salvo com sucesso!")