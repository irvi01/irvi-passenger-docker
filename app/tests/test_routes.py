import pytest
from app import app, db
from app.models import Item, User
import json
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


@pytest.fixture
def client():
    """Configura o cliente de teste e o banco de dados para os testes."""
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Banco em memória
    app.config["SECRET_KEY"] = "test_secret_key"

    with app.test_client() as client:
        with app.app_context():
            db.drop_all()  # Limpa as tabelas
            db.create_all()  # Recria as tabelas
        yield client


@pytest.fixture
def token(client):
    """Cria um usuário e retorna o token JWT."""
    client.post("/auth/register", json={"username": "testuser", "password": "1234"})
    response = client.post(
        "/auth/login", json={"username": "testuser", "password": "1234"}
    )
    data = json.loads(response.data)
    return data["token"]


def test_register_user(client):
    """Testa o registro de um novo usuário."""
    response = client.post(
        "/auth/register", json={"username": "newuser", "password": "password123"}
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["message"] == "Usuário criado com sucesso!"


def test_login_user(client):
    """Testa o login de um usuário existente."""
    client.post("/auth/register", json={"username": "testuser", "password": "1234"})
    response = client.post(
        "/auth/login", json={"username": "testuser", "password": "1234"}
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "token" in data


def test_get_items_empty(client, token):
    """Testa a listagem de itens quando não há itens."""
    response = client.get("/items", headers={"x-access-token": token})
    assert response.status_code == 200
    assert json.loads(response.data) == []


def test_create_item(client, token):
    """Testa a criação de um novo item."""
    response = client.post(
        "/items", headers={"x-access-token": token}, json={"name": "Item Teste"}
    )
    assert response.status_code == 201
    assert "Item adicionado!" in response.get_data(as_text=True)


def test_get_item_by_id(client, token):
    """Testa a busca de um item pelo ID."""
    client.post(
        "/items", headers={"x-access-token": token}, json={"name": "Item Teste"}
    )
    response = client.get("/items/1", headers={"x-access-token": token})
    assert response.status_code == 200
    assert "Item Teste" in response.get_data(as_text=True)


def test_update_item(client, token):
    """Testa a atualização de um item existente."""
    client.post(
        "/items", headers={"x-access-token": token}, json={"name": "Item Teste"}
    )
    response = client.put(
        "/items/1", headers={"x-access-token": token}, json={"name": "Item Atualizado"}
    )
    assert response.status_code == 200
    assert "Item atualizado com sucesso!" in response.get_data(as_text=True)


def test_delete_item(client, token):
    """Testa a exclusão de um item existente."""
    client.post(
        "/items", headers={"x-access-token": token}, json={"name": "Item Teste"}
    )
    response = client.delete("/items/1", headers={"x-access-token": token})
    assert response.status_code == 200
    assert "Item removido com sucesso!" in response.get_data(as_text=True)
