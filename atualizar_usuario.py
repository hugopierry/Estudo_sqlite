import sqlite3

conexao = sqlite3.connect("meu_banco.db") # cria banco de dados
cursor = conexao.cursor() # abre conexão


id_usuario = input("Digite o ID do usuário que você quer atualizar: ")
novo_email = input("Digite o novo email do usuário: ")

comando_update = "UPDATE usuarios SET email = ? WHERE id = ?"
cursor.execute(comando_update, (novo_email, id_usuario))


conexao.commit()
conexao.close()

if cursor.rowcount > 0:
    print(f"Usuário '{id_usuario}' atualizado com sucesso!")
else:
    print("Nenhum usuário encontrado com esse ID.")

