from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
import logging
import json_log_formatter

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configurações do Banco de Dados
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'app.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Chave secreta para geração de tokens JWT
app.config["SECRET_KEY"] = "091020@Dy"

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# Configuração de logs estruturados em JSON
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(json_handler)


# Logar cada requisição recebida
@app.before_request
def log_request_info():
    log_data = {
        "message": "Nova requisição recebida",
        "method": request.method,
        "url": request.url,
        "headers": {key: value for key, value in request.headers.items()},
        "body": request.get_data(as_text=True),
    }
    app.logger.info(log_data)


# Importação do monitoring e rotas do app
from app.monitoring import register_monitoring_routes
from app import routes

# Registro das rotas de monitoramento
register_monitoring_routes(app)
