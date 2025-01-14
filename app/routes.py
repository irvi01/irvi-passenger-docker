from flask import request, jsonify, send_from_directory
from app import app, db
from app.models import Item, User
import jwt
import datetime
from functools import wraps
from time import time


# Página inicial da aplicação.
@app.route("/")
def serve_frontend():
    return send_from_directory("static", "index.html")


# Decorador para verificar se o token JWT é válido
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("x-access-token")
        if not token:
            return jsonify({"error": "Token ausente"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data["id"]).first()
        except Exception:
            return jsonify({"error": "Token inválido"}), 401
        return f(current_user, *args, **kwargs)

    return decorated


# Rota para registrar um novo usuário
@app.route("/auth/register", methods=["POST"])
def register_user():
    """Rota para criar um novo usuário."""
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Nome de usuário e senha são obrigatórios"}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error": "Usuário já existe"}), 409

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return (
        jsonify(
            {"message": "Usuário criado com sucesso!", "username": new_user.username}
        ),
        201,
    )


# Rota para autenticar um usuário e retornar um token JWT
@app.route("/auth/login", methods=["POST"])
def login():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Nome de usuário e senha são obrigatórios"}), 400

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return jsonify({"error": "Credenciais inválidas"}), 401

        payload = {
            "id": str(user.id),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        }

        # Decodifica o token para string antes de retornar
        token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")
        if isinstance(token, bytes):
            token = token.decode("utf-8")

        return jsonify({"token": token})

    except Exception as e:
        app.logger.error(f"Erro na rota /auth/login: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500


# Rota para listar todos os itens
@app.route("/items", methods=["GET"])
@token_required
def get_items(current_user):
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name} for item in items])


# Rota para criar um novo item
@app.route("/items", methods=["POST"])
@token_required
def create_item(current_user):
    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "Nome do item é obrigatório"}), 400

    new_item = Item(name=name)
    db.session.add(new_item)
    db.session.commit()

    return (
        jsonify(
            {"message": "Item adicionado!", "id": new_item.id, "name": new_item.name}
        ),
        201,
    )


# Rota para buscar um item por ID
@app.route("/items/<int:item_id>", methods=["GET"])
@token_required
def get_item_by_id(current_user, item_id):
    item = db.session.get(Item, item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404
    return jsonify({"id": item.id, "name": item.name})


# Rota para atualizar um item
@app.route("/items/<int:item_id>", methods=["PUT"])
@token_required
def update_item(current_user, item_id):
    item = db.session.get(Item, item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    data = request.json
    item.name = data.get("name", item.name)
    db.session.commit()

    return jsonify(
        {"message": "Item atualizado com sucesso!", "id": item.id, "name": item.name}
    )


# Rota para deletar um item
@app.route("/items/<int:item_id>", methods=["DELETE"])
@token_required
def delete_item(current_user, item_id):
    item = db.session.get(Item, item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item removido com sucesso!", "id": item.id})
