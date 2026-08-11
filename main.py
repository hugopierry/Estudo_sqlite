import sqlite3

conexao = sqlite3.connect("meu_banco.db") # cria banco de dados
cursor = conexao.cursor() # abre conexão

# criar tabela
comando_sql = """ 
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)

"""

# executa comando
cursor.execute(comando_sql)

# salva comando
conexao.commit()

print("Banco de dados e tabela criados com  sucesso!")
#fecha conexão
conexao.close()



