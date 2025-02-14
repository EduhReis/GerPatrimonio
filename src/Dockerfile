# 1. Usa uma imagem base oficial do Python
FROM python:3.10

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia os arquivos do projeto para dentro do container
COPY . /app

# 4. Instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Executa o script seeder.py para popular o banco de dados
RUN python seeder.py

# 6. Expõe a porta usada pelo Flask (5000)
EXPOSE 5000

# 7. Define a variável de ambiente para rodar o Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# 8. Comando para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]