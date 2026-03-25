import sqlite3

conn = sqlite3.connect("data/webtoons.db")
cursor = conn.cursor()

# Ver tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tabelas:", cursor.fetchall())

# Ver dados
cursor.execute("SELECT * FROM webtoons")
rows = cursor.fetchall()

print("Quantidade de registros:", len(rows))

for row in rows[:5]:
    print(row)

conn.close()