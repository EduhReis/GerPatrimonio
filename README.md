# GerPatrimonio

### SISTEMA DE GERENCIAMENTO DE PATRIMÔNIO

---

> [!NOTE]
> Passos para realizar esse projeto:

- [ ] Listar Tecnologias a serem utilizadas
- [ ] Criar um Back end com as tecnologias e disponibilizar os passo-a-passo de como executar
- [ ] Criar uma Base de dados (Base local, ou usando o processamento do pc como o SQLite)
- [ ] Criar um Front end com as tecnologias utilizadas e passo-a-passo para utilizar
- [ ] Criar um vídeo executando o protótipo final

1. Padrões arquiteturais que são necessários:
   - MVC
   - REPOSITORIES 
2. Padrões de Boas práticas:
   - CLEAN CODE
   - DESIGN PATTERN (Esse aqui tem que estudar sobre Patterns pois é legal explicar o porque foi selecionado o Pattern)
3. Estrutura de Banco de dados:
   - ER (Entidade relacionamento)
   - Banco relacional (Será necessário relacionar corretamente cada entidade)
4. Documentação:
   - Ao final da prototipação, realizar uma documentação de tudo que foi feito, ensinando o usuário que ver o repositório a instalar e rodar.

## Descrição

GerPatrimonio é um sistema de gerenciamento de patrimônio desenvolvido em Python utilizando o framework Flask. Ele permite o cadastro, edição, listagem e exclusão de patrimônios e usuários, além de funcionalidades de autenticação e autorização.

## Tecnologias Utilizadas

### Backend
- **Linguagem:** Python
- **Framework:** Flask

### Frontend
- **Linguagem:** JavaScript
- **Frameworks:** Bootstrap, DataTables

### Banco de Dados
- **SQLite**
- **Postgres**

## Estrutura do Projeto

```
GerPatrimonio/
├── backend/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   ├── main_routes.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── bootstrap.bundle.min.js
│   │   │   ├── bootstrap.min.css
│   │   │   ├── datatables.min.css
│   │   │   ├── datatables.min.js
│   │   │   ├── styles.css
│   │   ├── js/
│   │   │   ├── datables.js
│   ├── templates/
│   │   ├── admin.html
│   │   ├── alterar_senha.html
│   │   ├── alterar_usuario.html
│   │   ├── base.html
│   │   ├── cadastro.html
│   │   ├── cadastro_modal.html
│   │   ├── editar.html
│   │   ├── listagem.html
│   │   ├── login.html
│   │   ├── register.html
├── infra/
│   ├── gerPatrimonio.db
│   ├── seederDb.py
├── venv/
├── run.py
├── seeder.py
├── test_crud.py
├── README.md
├── requirements.txt
```

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Virtualenv

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/GerPatrimonio.git
   cd GerPatrimonio
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script de seed para popular o banco de dados:
   ```bash
   python seeder.py
   ```

5. Inicie a aplicação:
   ```bash
   python run.py
   ```

6. Acesse a aplicação em `http://127.0.0.1:5000`.

## Uso

### Funcionalidades

- **Autenticação:** Login e logout de usuários.
- **Administração de Usuários:** Cadastro, edição, ativação, desativação e exclusão de usuários.
- **Gerenciamento de Patrimônios:** Cadastro, edição, listagem e exclusão de patrimônios.
- **Controle de Acesso:** Apenas usuários com cargos de "Admin" ou "Supervisor" podem criar, editar ou apagar patrimônios. Usuários com cargos inferiores têm acesso restrito a essas funcionalidades.

### Rotas Principais

- `/login`: Página de login.
- `/admin`: Página de administração de usuários (apenas para administradores).
- `/listagem`: Página de listagem de patrimônios.
- `/cadastro`: Página de cadastro de patrimônio.
- `/editar/<id>`: Página de edição de patrimônio.
- `/apagar/<id>`: Rota para apagar um patrimônio.

## Estrutura das Pastas

### backend

Contém os arquivos principais do backend da aplicação.

- `__init__.py`: Inicializa o aplicativo Flask e configura o banco de dados.
- `models.py`: Define os modelos de dados usando SQLAlchemy.
- `routes/`: Contém os arquivos de rotas para a aplicação.
  - `__init__.py`: Inicializa o blueprint das rotas.
  - `auth_routes.py`: Define as rotas de autenticação e administração.
  - `main_routes.py`: Define as rotas principais da aplicação.
- `static/`: Contém arquivos estáticos como CSS e JavaScript.
  - `css/`: Contém arquivos CSS e JavaScript relacionados ao DataTables e Bootstrap.
  - `js/`: Contém arquivos JavaScript personalizados.
- `templates/`: Contém os templates HTML para a aplicação.

### infra

Contém os arquivos de infraestrutura para a aplicação.

- `gerPatrimonio.db`: Banco de dados SQLite da aplicação.
- `seederDb.py`: Script para popular o banco de dados com dados iniciais.

### venv

Ambiente virtual Python.

### run.py

Script para iniciar a aplicação Flask.

### seeder.py

Script para popular o banco de dados com dados iniciais.

### test_crud.py

Script de testes unitários para as operações CRUD.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/fooBar`).
3. Faça commit das suas alterações (`git commit -am 'Add some fooBar'`).
4. Faça push para a branch (`git push origin feature/fooBar`).
5. Crie um novo Pull Request.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Contato

Link do Projeto: [https://github.com/EduhReis/GerPatrimonio]

DEV SR DAVEZ 🤠👍
