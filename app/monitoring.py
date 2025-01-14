from flask import Response, jsonify, request
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from app import db
from app.models import User, Item
import psutil
from time import time
from sqlalchemy import text

# Métricas Prometheus
REQUEST_COUNT = Counter('http_requests_total', 'Total de requisições HTTP', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Duração das requisições HTTP', ['method', 'endpoint'])
TOTAL_USERS = Gauge('total_users', 'Número total de usuários registrados')
TOTAL_ITEMS = Gauge('total_items', 'Número total de itens armazenados')
CPU_USAGE = Gauge('cpu_usage_percent', 'Uso de CPU em porcentagem')
MEMORY_USAGE = Gauge('memory_usage_bytes', 'Uso de memória em bytes')

def update_custom_metrics():
    """Atualiza métricas customizadas."""
    TOTAL_USERS.set(User.query.count())
    TOTAL_ITEMS.set(Item.query.count())
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().used)

def register_monitoring_routes(app):
    """Registra rotas relacionadas ao monitoramento."""

    @app.before_request
    def start_timer():
        """Inicia o temporizador manualmente."""
        request.start_time = time()

    @app.after_request
    def log_request(response):
        """Calcula a duração e registra métricas no Prometheus."""
        if request.endpoint != 'metrics' and request.endpoint:
            REQUEST_COUNT.labels(request.method, request.endpoint, response.status_code).inc()
            request_latency = time() - request.start_time
            REQUEST_LATENCY.labels(request.method, request.endpoint).observe(request_latency)
        return response

    @app.before_request
    def update_metrics_before_request():
        """Atualiza métricas customizadas antes de cada requisição."""
        update_custom_metrics()

    @app.route('/metrics', methods=['GET'])
    def metrics():
        """Expor métricas Prometheus."""
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

    @app.route('/health', methods=['GET'])
    def health_check():
        """Verificar saúde do sistema."""
        try:
            db.session.execute(text('SELECT 1'))
            return jsonify({"status": "healthy"}), 200
        except Exception as e:
            app.logger.error(f"Erro na verificação de saúde: {e}")
            return jsonify({"status": "unhealthy", "error": str(e)}), 500
