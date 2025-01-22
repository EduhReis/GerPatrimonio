import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('gerarpatrimonio.db')

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

# Inserir dados iniciais na tabela patrimonio
cursor.executemany('''
INSERT INTO patrimonio (nome, categoria, status)
VALUES (?, ?, ?)
''', [
    ('Computador', 'Eletrônico', 'Em uso'),
    ('Impressora', 'Eletrônico', 'Manutenção'),
    ('Mesa de Escritório', 'Mobiliário', 'Em uso')
])

# Inserir dados iniciais na tabela funcionario
cursor.executemany('''
INSERT INTO funcionario (nome, cpf, cargo, telefone)
VALUES (?, ?, ?, ?)
''', [
    ('João Silva', '12345678901', 'Técnico', '11999999999'),
    ('Maria Oliveira', '98765432100', 'Gerente', '21988888888'),
    ('Carlos Souza', '45612378900', 'Assistente', '31977777777')
])



# Confirmar as alterações
conexao.commit()

print("Tabela criada com sucesso!")

# Fechar a conexão
conexao.close()