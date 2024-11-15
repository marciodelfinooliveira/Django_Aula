# Usando uma imagem Python leve como base
FROM python:3.11.2-slim-bullseye

# Define o diretório de trabalho dentro do container
WORKDIR /code

# Copia o arquivo de dependências e instala as bibliotecas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto para o container
COPY . .

# Expõe a porta usada pelo servidor de desenvolvimento
EXPOSE 8000

# Comando padrão para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
