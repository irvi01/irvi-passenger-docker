from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configurações do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Chave secreta para geração de tokens JWT
app.config['SECRET_KEY'] = '091020@Dy'

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

from app import routes
