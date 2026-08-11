import sqlite3

conexao = sqlite3.connect("meu_banco.db") # cria banco de dados
cursor = conexao.cursor() # abre conexão

resposta = "S"
while resposta == "S":
        print("\n=== INSERÇÃO DE USUÁRIOS NO BANCO DE DADOS ===")
        nome = input("\nDigite o nome: ")
        email = input("Digite o email: ")

        resposta = input("Continuar? [S/N]: ").upper()
       
print("Inserções finalizadas com sucesso!")
             

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