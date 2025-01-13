# Imagem base
FROM ubuntu:20.04

# Instalar dependências essenciais
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    python3 \
    python3-pip \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Instalar Passenger
RUN curl -sSL https://oss-binaries.phusionpassenger.com/auto-software-signing-gpg-key.asc \
    -o /usr/share/keyrings/passenger-archive-keyring.gpg && \
    echo "deb [trusted=yes] https://oss-binaries.phusionpassenger.com/apt/passenger focal main" \
    > /etc/apt/sources.list.d/passenger.list && \
    apt-get update && apt-get install -y passenger

# Criar alias para python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Definir o diretório de trabalho
WORKDIR /opt/app

# Copiar os arquivos do projeto para o container
COPY . /opt/app

# Instalar dependências Python
RUN pip3 install -r /opt/app/app/requirements.txt

# Configurar o PYTHONPATH e saída de logs sem buffer
ENV PYTHONPATH=/opt/app
ENV PYTHONUNBUFFERED=1

# Configurar o Passenger para rodar a aplicação
CMD ["passenger", "start", "--port", "80", "--app-type", "python", "--startup-file", "passenger_wsgi.py"]
