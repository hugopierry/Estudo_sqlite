import sqlite3

conexao = sqlite3.connect("meu_banco.db") # cria banco de dados
cursor = conexao.cursor() # abre conexão

nome = input("Digite o nome: ")
email = input("Digite o email: ")

comando_sql = f"INSERT INTO usuarios (nome, email) VALUES (?, ?)"

try:
    cursor.execute(comando_sql, (nome, email))
    conexao.commit()

    
    print(f"Usuário '{nome}' inserido com sucesso!")
except sqlite3.IntegrityError:
    print("Erro: Email já cadastrado!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


conexao.close()