import sqlite3

conexao = sqlite3.connect("meu_banco.db") # cria banco de dados
cursor = conexao.cursor() # abre conexão

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()
print("-" * 75)
print("LISTA DE USUÁRIOS CADASTRADOS:".center(70))
print("-" * 75)
for usuario in usuarios:
    print(f"ID: {usuario[0]:<5} | Nome: {usuario[1]:<20} | Email: {usuario[2]}")

print("-" * 75)
print(f"Total de usuários cadastrados: {len(usuarios)}")
conexao.close()
