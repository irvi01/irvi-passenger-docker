import json
import pytest
from prometheus_client.parser import text_string_to_metric_families
from app.monitoring import update_custom_metrics
from app import app
from sqlalchemy import text
from prometheus_client import REGISTRY, Counter, Histogram, Gauge

def reset_metrics():
    """Reseta apenas métricas customizadas definidas no projeto."""
    metrics_to_reset = {'total_users', 'total_items', 'http_requests_total', 'http_request_duration_seconds'}
    for collector_name, collector in list(REGISTRY._names_to_collectors.items()):
        if collector_name in metrics_to_reset:
            REGISTRY.unregister(collector)


def test_metrics_endpoint(client):
    """Teste para verificar o funcionamento do endpoint /metrics."""
    response = client.get('/metrics')
    assert response.status_code == 200
    assert 'text/plain' in response.content_type

def test_health_endpoint(client):
    """Teste para verificar o funcionamento do endpoint /health."""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['status'] == 'healthy'

def test_total_users_metric(client, mocker):
    """Teste para verificar a métrica total_users."""
    reset_metrics()  # Reseta as métricas antes do teste
    mocker.patch('app.models.User.query.count', return_value=5)  # Mocka a contagem de usuários
    update_custom_metrics()  # Atualiza manualmente as métricas
    response = client.get('/metrics')
    for family in text_string_to_metric_families(response.data.decode('utf-8')):
        if family.name == 'total_users':
            for sample in family.samples:
                assert sample.value == 5

def test_total_items_metric(client, mocker):
    """Teste para verificar a métrica total_items."""
    reset_metrics()  # Reseta as métricas antes do teste
    mocker.patch('app.models.Item.query.count', return_value=10)  # Mocka a contagem de itens
    update_custom_metrics()  # Atualiza manualmente as métricas
    response = client.get('/metrics')
    for family in text_string_to_metric_families(response.data.decode('utf-8')):
        if family.name == 'total_items':
            for sample in family.samples:
                assert sample.value == 10
