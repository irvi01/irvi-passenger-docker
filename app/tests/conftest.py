import pytest
from app import app, db


@pytest.fixture
def client():
    """Cria um cliente de teste para o Flask."""
    with app.test_client() as client:
        with app.app_context():
            # Configuração do banco de dados para testes
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()
