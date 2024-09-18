# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o timezone para o Brasil (America/Sao_Paulo)
ENV TZ=America/Sao_Paulo
RUN apt-get update && apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Instale o Nginx
RUN apt-get update && apt-get install -y nginx apache2-utils

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo da pasta src para o diretório de trabalho
COPY src/ src/

# Copie o arquivo plombery.db para o diretório de trabalho
COPY plombery.db .

# Copie o arquivo de configuração do Nginx para o diretório de configuração do Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copie o arquivo .htpasswd para a pasta do Nginx
COPY .htpasswd /etc/nginx/.htpasswd

# Exponha a porta 80 para o Nginx
EXPOSE 80

# Exponha a porta 8001 para a aplicação Python
EXPOSE 8001

# Defina o comando padrão para iniciar o Nginx e a aplicação Python
CMD ["sh", "-c", "nginx && python src/main.py"]
