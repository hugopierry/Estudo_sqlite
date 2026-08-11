import sqlite3

conexao = sqlite3.connect("meu_banco.db") # cria banco de dados
cursor = conexao.cursor() # abre conexão

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

print("LISTA DE USUÁRIOS CADASTRADOS: ")
for usuario in usuarios:
    print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")

conexao.close()
