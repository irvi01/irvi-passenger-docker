import pytest
from app import app, db
from app.models import Item

@pytest.fixture
def client():
    """Fixture para configurar o cliente de teste do Flask."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria as tabelas antes de cada teste
        yield client

def test_home_route(client):
    """Testa a rota inicial '/'."""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Olá, Irvi! Sua aplicação Python está rodando no Passenger!"

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
