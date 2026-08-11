import sqlite3

conexao = sqlite3.connect("meu_banco.db") # cria banco de dados
cursor = conexao.cursor() # abre conexão

id_busca = input("Digite o ID do usuário: ")

comando_sql = "SELECT nome, email FROM usuarios WHERE id = ?"
cursor.execute(comando_sql, (id_busca, ))

usuario = cursor.fetchone()
conexao.close()

if usuario:
    print(f"Usuário encontrado: {usuario[0]}\n"
          f"email: ({usuario[1]})")
else:
    print(f"Usuário '{id_busca}' não encontrado!")

