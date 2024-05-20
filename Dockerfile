# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo da pasta src para o diretório de trabalho
COPY src/ src/

# Copie o arquivo plumbery.db para o diretório de trabalho
COPY plombery.db .

# Defina o comando padrão para executar a aplicação
CMD ["python", "src/main.py"]
