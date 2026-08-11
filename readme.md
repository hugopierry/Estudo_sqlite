# 🗄️ Estudos de CRUD com Python e SQLite3

Repositório criado para registrar meus estudos práticos de **Banco de Dados utilizando Python e SQLite3**, com foco nos conceitos fundamentais de **CRUD**.

Os exercícios deste repositório foram desenvolvidos durante meus estudos sobre integração entre Python e bancos de dados, utilizando o módulo nativo `sqlite3`.

> 📚 **Base de estudo:** Leandro Hirt | Academify
> 🐍 **Linguagem:** Python
> 🗄️ **Banco de dados:** SQLite3
> 🎯 **Foco:** CRUD e integração Python + Banco de Dados

---

## 🎯 Objetivo

O objetivo deste estudo é aprender, de forma prática, como uma aplicação Python pode **criar, armazenar, consultar, atualizar e excluir dados em um banco de dados SQLite**.

Este repositório representa uma etapa dos meus estudos de Banco de Dados e servirá como base para uma aplicação maior que pretendo desenvolver futuramente.

---

## 📚 Conteúdos estudados

Durante os exercícios, foram praticados os seguintes conceitos:

* Conexão com banco de dados utilizando `sqlite3`
* Criação de banco de dados
* Criação de tabelas
* `CREATE TABLE`
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* `WHERE`
* `PRIMARY KEY`
* `AUTOINCREMENT`
* `NOT NULL`
* `UNIQUE`
* `commit()`
* `cursor`
* `fetchone()`
* `rowcount`
* Parâmetros com `?`
* Tratamento de exceções com `try/except`
* `sqlite3.IntegrityError`
* Encerramento da conexão com `close()`

---

# 🔄 CRUD

CRUD é uma sigla utilizada para representar as quatro operações fundamentais realizadas sobre dados:

| Operação   | SQL      | Objetivo            |
| ---------- | -------- | ------------------- |
| **Create** | `INSERT` | Criar/inserir dados |
| **Read**   | `SELECT` | Consultar dados     |
| **Update** | `UPDATE` | Atualizar dados     |
| **Delete** | `DELETE` | Excluir dados       |

---

## 1. 🏗️ Criação do banco e da tabela

O primeiro exercício cria o banco de dados `meu_banco.db` e uma tabela chamada `usuarios`.

A tabela possui:

* `id` como chave primária;
* `nome` como texto obrigatório;
* `email` como texto obrigatório e único.

```python
import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

comando_sql = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
"""

cursor.execute(comando_sql)

conexao.commit()
conexao.close()
```

### Conceitos praticados

* `sqlite3.connect()`
* `cursor()`
* `CREATE TABLE IF NOT EXISTS`
* `PRIMARY KEY`
* `AUTOINCREMENT`
* `NOT NULL`
* `UNIQUE`
* `commit()`
* `close()`

---

# 2. ➕ Create — Inserindo usuários

Neste exercício, foi praticada a inserção de novos usuários utilizando `INSERT INTO`.

Os dados são recebidos através do `input()`.

```python
nome = input("Digite o nome: ")
email = input("Digite o email: ")

comando_sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"

cursor.execute(comando_sql, (nome, email))
conexao.commit()
```

Também foi utilizado tratamento de erros para impedir o cadastro de um e-mail que já exista na tabela.

```python
try:
    cursor.execute(comando_sql, (nome, email))
    conexao.commit()

except sqlite3.IntegrityError:
    print("Erro: Email já cadastrado!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

### Conceitos praticados

* `INSERT INTO`
* `VALUES`
* parâmetros `?`
* tuplas de parâmetros
* `try/except`
* `sqlite3.IntegrityError`
* `commit()`

---

# 3. 🔍 Read — Consultando usuários

Neste exercício, foi utilizado `SELECT` para consultar um usuário específico através do seu `id`.

```python
id_busca = input("Digite o ID do usuário: ")

comando_sql = "SELECT nome, email FROM usuarios WHERE id = ?"

cursor.execute(comando_sql, (id_busca,))

usuario = cursor.fetchone()
```

O método `fetchone()` retorna o primeiro registro encontrado.

Depois, o programa verifica se o usuário foi encontrado:

```python
if usuario:
    print(f"Usuário encontrado: {usuario[0]}")
    print(f"Email: {usuario[1]}")
else:
    print(f"Usuário '{id_busca}' não encontrado!")
```

### Conceitos praticados

* `SELECT`
* `FROM`
* `WHERE`
* `fetchone()`
* consulta por `id`
* verificação de resultado

---

# 4. ✏️ Update — Atualizando usuários

Neste exercício, foi praticada a atualização de dados utilizando `UPDATE`.

O exemplo atualiza o e-mail de um usuário através do seu `id`.

```python
id_usuario = input("Digite o ID do usuário que você quer atualizar: ")
novo_email = input("Digite o novo email do usuário: ")

comando_update = "UPDATE usuarios SET email = ? WHERE id = ?"

cursor.execute(comando_update, (novo_email, id_usuario))

conexao.commit()
```

Também foi utilizado `rowcount` para verificar se algum registro realmente foi alterado.

```python
if cursor.rowcount > 0:
    print(f"Usuário '{id_usuario}' atualizado com sucesso!")
else:
    print("Nenhum usuário encontrado com esse ID.")
```

### Conceitos praticados

* `UPDATE`
* `SET`
* `WHERE`
* atualização utilizando `id`
* `rowcount`
* `commit()`

---

# 5. 🗑️ Delete — Excluindo usuários

O último exercício do CRUD utiliza `DELETE` para remover um usuário através do seu `id`.

```python
id_para_deletar = input(
    "Digite o ID do usuário que você deseja excluir: "
)

comando_deletar = "DELETE FROM usuarios WHERE id = ?"

cursor.execute(comando_deletar, (id_para_deletar,))

conexao.commit()
```

Assim como no `UPDATE`, foi utilizado `rowcount` para verificar se algum registro foi excluído.

```python
if cursor.rowcount > 0:
    print(f"Usuário '{id_para_deletar}' deletado com sucesso!")
else:
    print("Nenhum usuário encontrado com esse ID.")
```

### Conceitos praticados

* `DELETE FROM`
* `WHERE`
* exclusão por `id`
* `rowcount`
* `commit()`

---

# 🧠 O que aprendi

Com esses exercícios, pratiquei o fluxo básico de uma aplicação Python trabalhando com banco de dados:

```text
Python
   ↓
sqlite3
   ↓
Banco de Dados SQLite
   ↓
Tabela usuarios
   ↓
CRUD
```

Também comecei a entender que o banco de dados permite que os dados permaneçam armazenados mesmo depois que o programa é encerrado.

---

# 📂 Estrutura dos estudos

Uma possível organização dos arquivos é:

```text
Estudo_sqlite/
│
├── criar_banco.py
├── inserir_usuario.py
├── buscar_usuario.py
├── atualizar_usuario.py
├── deletar_usuario.py
│
└── meu_banco.db
```

> O arquivo `.db` é criado pelo SQLite durante a execução dos programas.

---

# 🚀 Próximo passo: Mini WMS

Este estudo de SQLite3 não é o ponto final.

A próxima etapa será aplicar os conhecimentos adquiridos em um projeto maior: meu **Mini WMS desenvolvido em Python**.

A ideia é integrar um banco de dados ao sistema para armazenar de forma persistente informações como:

* 👤 Usuários
* 📦 Produtos
* 📊 Estoque
* 🔄 Movimentações
* 🔐 Dados relacionados ao sistema de login

O objetivo será evoluir de programas isolados de estudo para uma aplicação Python utilizando **POO + SQLite3 + CRUD** de maneira integrada.

```text
ESTUDOS
   │
   ├── Python
   │
   ├── SQL
   │
   └── SQLite3 + CRUD
          │
          ▼
      MINI WMS
          │
          ├── Login
          ├── Usuários
          ├── Produtos
          ├── Estoque
          └── Movimentações
```

---

# 📌 Status do estudo

**Concluído:**

* [x] Conexão com SQLite3
* [x] Criação do banco
* [x] Criação da tabela
* [x] INSERT
* [x] SELECT
* [x] UPDATE
* [x] DELETE
* [x] Tratamento de erros
* [x] Parâmetros SQL
* [x] `commit()`
* [x] `fetchone()`
* [x] `rowcount`

**Próxima etapa:**

* [ ] Integrar SQLite3 ao Mini WMS
* [ ] Criar banco do Mini WMS
* [ ] Persistir produtos
* [ ] Persistir usuários
* [ ] Integrar CRUD ao sistema
* [ ] Trabalhar com relacionamentos entre tabelas
* [ ] Evoluir o banco conforme o projeto crescer

---

## 📖 Referência de estudo

**Leandro Hirt | Academify**

Este repositório foi criado como parte do meu processo de aprendizado e prática em **Python, SQL, SQLite3 e Banco de Dados**.

---

## 👨‍💻 Sobre o projeto

Este é um **repositório de estudos** criado para acompanhar minha evolução na programação.

A proposta é aprender os conceitos, praticá-los através de pequenos exercícios e posteriormente aplicar esse conhecimento em projetos maiores e mais próximos de situações reais.

**Python + Banco de Dados + prática = evolução.**
