from flask import request, jsonify
from app.models import Item
from app import app, db

@app.route('/')
def home():
    return jsonify({
        "message": "Olá, Irvi! Sua aplicação Python está rodando no Passenger!",
        "endpoints": [
            {"method": "GET", "route": "/items", "description": "Listar todos os itens."},
            {"method": "POST", "route": "/items", "description": "Adicionar um novo item."},
            {"method": "DELETE", "route": "/items/<int:item_id>", "description": "Remover um item pelo ID."}
        ]
    })

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([
        {"id": item.id, "name": item.name} for item in items
    ]), 200

@app.route('/items', methods=['POST'])
def add_item():
    item_name = request.json.get('name')
    if not item_name:
        return jsonify({"error": "O campo 'name' é obrigatório."}), 400

    new_item = Item(name=item_name)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item adicionado com sucesso!", "id": new_item.id, "name": new_item.name}), 201

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item removido com sucesso!", "id": item.id}), 200
