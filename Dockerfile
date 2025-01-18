# Imagem base
FROM ubuntu:20.04

# Instalar dependências essenciais
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    python3 \
    python3-pip \
    python3-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Instalar Passenger
RUN curl -sSL https://oss-binaries.phusionpassenger.com/auto-software-signing-gpg-key.asc \
    -o /usr/share/keyrings/passenger-archive-keyring.gpg && \
    echo "deb [trusted=yes] https://oss-binaries.phusionpassenger.com/apt/passenger focal main" \
    > /etc/apt/sources.list.d/passenger.list && \
    apt-get update && apt-get install -y passenger

# Instalar Node.js (versão 18.x)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

# Criar alias para python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Definir o diretório de trabalho
WORKDIR /opt/app

# Copiar apenas o arquivo de requisitos inicialmente para cache eficiente
COPY app/requirements.txt /opt/app/app/requirements.txt
RUN pip3 install -r /opt/app/app/requirements.txt

# Copiar arquivos de dependências do Node.js
COPY package.json package-lock.json /opt/app/
RUN npm install

# Copiar o restante do código do projeto
COPY . /opt/app

# Configurar o PYTHONPATH e saída de logs sem buffer
ENV PYTHONPATH=/opt/app
ENV PYTHONUNBUFFERED=1
ENV PASSENGER_LOG_FILE=/dev/stdout

# Build argument para passar a versão da tag (usada apenas para documentar)
ARG APP_VERSION=latest
LABEL version=$APP_VERSION
LABEL description="Imagem da aplicação com versão dinâmica via pipeline."

# Expor a porta 80
EXPOSE 80

# Configurar o Passenger para rodar a aplicação
CMD ["passenger", "start", "--port", "80", "--app-type", "python", "--startup-file", "passenger_wsgi.py"]
