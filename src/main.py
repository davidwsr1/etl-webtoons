from extract import extrair_webtoons
from transform import transformar
from load import salvar_csv, salvar_sqlite
from ai import gerar_resumo


def main():
    print("Extraindo dados...")
    dados = extrair_webtoons()

    print("Transformando dados...")
    dados_tratados = transformar(dados)

    print("Salvando dados...")
    salvar_csv(dados_tratados)
    salvar_sqlite(dados_tratados)

    print("ETL finalizada!")

    print("\nResumos gerados:\n")

    for item in dados_tratados[:5]:
        resumo = gerar_resumo(item)
        print("-----")
        print(resumo)

if __name__ == "__main__":
    main()