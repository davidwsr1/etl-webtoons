import pandas as pd
import sqlite3


def salvar_csv(dados):
    df = pd.DataFrame(dados)
    df.to_csv("data/webtoons.csv", index=False, encoding="utf-8")
    print("CSV salvo com sucesso!")


def salvar_sqlite(dados):
    conn = sqlite3.connect("data/webtoons.db")

    df = pd.DataFrame(dados)
    df.to_sql("webtoons", conn, if_exists="replace", index=False)

    conn.close()
    print("Dados salvos no SQLite!")