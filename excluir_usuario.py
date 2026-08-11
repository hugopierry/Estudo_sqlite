import sqlite3

conexao = sqlite3.connect("meu_banco.db") # cria banco de dados
cursor = conexao.cursor() # abre conexão

id_para_deletar = input("Digite o ID do usuário que você deseja excluir: ")


comando_deletar = "DELETE FROM usuarios WHERE id = ?"
cursor.execute(comando_deletar, (id_para_deletar, ))

conexao.commit()
conexao.close()
if cursor.rowcount > 0:
    print(f"Usuário '{id_para_deletar}' deletado com sucesso!")
else:
    print("Nenhum usuário encontrado com esse ID.")