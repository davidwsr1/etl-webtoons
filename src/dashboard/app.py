import streamlit as st
import sqlite3
import pandas as pd

# conexão com banco
conn = sqlite3.connect("data/webtoons.db")

# carregar dados
df = pd.read_sql("SELECT * FROM webtoons", conn)

st.title(" Dashboard das Webtoons")

# mostrar tabela
st.subheader(" Dados coletados")
st.dataframe(df)

# filtro por gênero
genero = st.selectbox("Escolha um gênero", df["genero"].unique())

df_filtrado = df[df["genero"] == genero]

st.subheader(f" Webtoons de {genero}")
st.dataframe(df_filtrado)

# top 10
top10 = df.sort_values(by="likes", ascending=False).head(10)

st.subheader("🔥 Top Webtoons do momento")
st.bar_chart(top10.set_index("titulo")["likes"])

# função de resumo (IA fake)
def gerar_resumo(webtoon):
    if webtoon["likes"] > 1000000:
        popularidade = "um grande sucesso"
    else:
        popularidade = "bem avaliado"

    return f"{webtoon['titulo']} é um webtoon de {webtoon['genero']} com {webtoon['likes']} likes, sendo {popularidade}."

# mostrar recomendações
st.subheader("Recomendações com IA")

for _, row in top10.iterrows():
    st.write("-----")
    st.write(gerar_resumo(row))