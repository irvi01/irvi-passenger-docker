import pytest
from app import app

@pytest.fixture
def client():
    """Fixture para configurar o cliente de teste do Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Testa a rota inicial '/'."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Ola, Irvi!" in response.data

def test_items_get_empty(client):
    """Testa a rota '/items' quando o banco está vazio."""
    response = client.get('/items')
    assert response.status_code == 200
    assert response.json == []

def test_items_post(client):
    """Testa a criação de um item."""
    response = client.post('/items', json={"name": "Item Teste"})
    assert response.status_code == 201
    data = response.json
    assert data["message"] == "Item adicionado com sucesso!"
    assert data["name"] == "Item Teste"
