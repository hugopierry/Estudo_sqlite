import sqlite3

conexao = sqlite3.connect("meu_banco.db")  # cria/abre o banco de dados
cursor = conexao.cursor()  # cria o cursor

# Adiciona a coluna "poder" na tabela usuarios

comando_sql = """
ALTER TABLE usuarios
DROP COLUMN poder;
"""

# Executa o comando
cursor.execute(comando_sql)

# Salva a alteração
conexao.commit()

print("Coluna 'poder' adicionada com sucesso!")

# Fecha a conexão
conexao.close()