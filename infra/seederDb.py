import sqlite3
import os

# Conectar ao banco de dados ou criar um novo
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../infra/gerPtrimonio.db'))
conexao = sqlite3.connect(db_path)

cursor = conexao.cursor()
# Criar a tabela patrimonio
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patrimonio(
        id_patrimonio INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        categoria VARCHAR(20),
        status VARCHAR(20)
               

    )
''')

# Criar a tabela funcionario
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionario (
    id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL,
    cpf DECIMAL(11) UNIQUE NOT NULL,
    cargo VARCHAR(20) NOT NULL,
    telefone DECIMAL(12)
)
''')




# Confirmar as alterações
conexao.commit()

print("Tabela criada com sucesso!")

# Fechar a conexão
conexao.close()