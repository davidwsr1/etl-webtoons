# ETL Webtoon Analytics

Pipeline de Engenharia de Dados desenvolvido em Python e PySpark para extração, transformação e análise de dados de Webtoons utilizando a arquitetura Medallion (Bronze, Silver e Gold).

## Objetivo

Construir uma pipeline ETL completa capaz de:

* Extrair dados do ranking de Webtoons utilizando Selenium.
* Armazenar os dados brutos na camada Bronze.
* Realizar limpeza e padronização com PySpark na camada Silver.
* Gerar dados analíticos na camada Gold.
* Demonstrar conceitos de Engenharia de Dados, Spark e Data Lake.

---

## Tecnologias Utilizadas

* Python
* Selenium
* Pandas
* PySpark
* Apache Spark
* Apache Airflow (estrutura preparada)
* CSV
* Arquitetura Medallion

---

## Arquitetura

```text
Webtoon Ranking
       │
       ▼
Extração (Selenium)
       │
       ▼
Bronze (Raw Data)
       │
       ▼
Silver (Dados Tratados)
       │
       ▼
Gold (Dados Analíticos)
```

---

## Estrutura do Projeto

```text
ETL-Webtoon/
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── dags/
│   └── etl_webtoon_dag.py
│
├── src/
│   ├── extract/
│   │   └── extract.py
│   │
│   ├── load/
│   │   └── load.py
│   │
│   ├── spark/
│   │   └── spark_session.py
│   │
│   ├── transform/
│   │   ├── bronze_to_silver.py
│   │   └── silver_to_gold.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## Camada Bronze

Armazena os dados exatamente como foram extraídos da fonte.

Exemplo:

| titulo                  | genero        | likes |
| ----------------------- | ------------- | ----- |
| My Giant Nerd Boyfriend | Slice of Life | 77.9M |

---

## Camada Silver

Realiza:

* Limpeza de dados
* Remoção de duplicidades
* Conversão de likes para formato numérico
* Padronização de textos
* Inclusão de metadados de processamento

---

## Camada Gold

Gera datasets analíticos:

### Top Webtoons

Ranking dos Webtoons mais populares.

### Likes por Gênero

Quantidade total de likes agrupada por gênero.

### Gêneros Mais Populares

Classificação dos gêneros com maior engajamento.

---

## Como Executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar pipeline

```bash
python src/main.py
```

---

## Resultados

A pipeline realiza:

1. Extração automática do ranking Webtoon.
2. Armazenamento na camada Bronze.
3. Processamento utilizando PySpark.
4. Geração de datasets analíticos na camada Gold.

---

## Próximas Evoluções

* Integração com Google Cloud Storage (GCS)
* Processamento em Dataproc
* Armazenamento em BigQuery
* Orquestração com Cloud Composer (Airflow)
* Dashboard em Looker Studio
* Processamento em Streaming

---

## Autor

David Rocha

Estudante de Análise e Desenvolvimento de Sistemas – PUC Minas.
