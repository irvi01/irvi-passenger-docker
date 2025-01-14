# **Irvi Passenger Application**

## **Sobre o Projeto**
Este repositório é um exemplo completo de aplicação **CRUD** integrada com autenticação JWT, logs estruturados e monitoramento utilizando Prometheus e Grafana. O objetivo é aprender durante a crição de um ambiente próximo ao de produção, com boas práticas de desenvolvimento e DevOps.

---

## **Funcionalidades**
- 🌐 API RESTful utilizando **Flask**.
- 🔑 Autenticação JWT.
- 🛠️ Operações completas de CRUD.
- 📊 Monitoramento de métricas via Prometheus.
- 📈 Dashboard configurável no Grafana.
- 🧪 Testes automatizados com **pytest**.
- 🔄 CI/CD utilizando GitHub Actions para build, testes e publicação.

---

## **Tecnologias Utilizadas**
- **Python** (Flask, SQLAlchemy)
- **Docker**
- **Prometheus** e **Grafana**
- **GitHub Actions**

---

## **Estrutura do Projeto**
```plaintext
irvi-passenger-docker/
├── app/
│   ├── __init__.py            # Configuração inicial do Flask e logs
│   ├── models.py              # Definição de modelos (ORM)
│   ├── routes.py              # Definição de rotas (CRUD e autenticação)
│   ├── monitoring.py          # Métricas e monitoramento
│   ├── requirements.txt       # Dependências da aplicação
│   ├── tests/                 # Testes automatizados
│   │   ├── __init__.py        # Inicialização dos testes
│   │   ├── test_routes.py     # Testes das rotas CRUD
│   │   └── test_monitoring.py # Testes do monitoramento
├── static/                    # Arquivos frontend (HTML, CSS, JS)
├── templates/                 # Templates HTML (frontend integrado)
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline CI/CD
├── Dockerfile                 # Configuração da imagem Docker
├── docker-compose.yml         # Orquestração do Docker
├── prometheus.yml             # Configuração do Prometheus
├── main.py                    # Arquivo principal para inicializar a aplicação
├── passenger_wsgi.py          # Integração com Passenger
└── README.md                  # Documentação do projeto
```

---

## **Configuração do Ambiente**

### **Requisitos**
- 🐋 Docker e Docker Compose instalados.
- 🔗 Git configurado.

### **Clonar o Repositório**
```bash
git clone https://github.com/irvi01/irvi-passenger-docker.git
cd irvi-passenger-docker
```

---

## **Como Usar**

### **Executar o Projeto com Docker Compose**
Para iniciar todos os serviços (app, Prometheus e Grafana):
```bash
docker-compose up --build
```
A aplicação estará disponível em [http://localhost:8080](http://localhost:8080).

### **Acessar o Grafana**
- URL: [http://localhost:3000](http://localhost:3000)
- Usuário: `admin`
- Senha: `admin`

### **Acessar o Prometheus**
- URL: [http://localhost:9090](http://localhost:9090)

---

## **Testes Automatizados**

### **Executar Testes Localmente**
1. Certifique-se de que as dependências estão instaladas:
   ```bash
   pip install -r app/requirements.txt
   ```
2. Execute os testes:
   ```bash
   pytest app/tests/
   ```

### **Executar Testes no Docker**
```bash
docker-compose run app pytest app/tests/
```

---

## **Monitoramento e Logs**

### **Métricas Disponíveis**
- **HTTP Requests:**
  - Total de requisições HTTP.
  - Latência das requisições.
- **Métricas Customizadas:**
  - Total de usuários cadastrados.
  - Total de itens no sistema.
  - Uso de CPU e memória do sistema.

### **Exposição de Métricas**
As métricas estão disponíveis no endpoint:
```plaintext
GET /metrics
```

---

## **Frontend**

### **Páginas Disponíveis**
1. **Login e Registro:**
   - Página inicial para criação de conta e login.
2. **CRUD:**
   - Gerenciamento de itens: criar, listar, atualizar e deletar itens.

### **Como Acessar**
- Login e Registro: [http://localhost:8080](http://localhost:8080)
- CRUD: Disponível após login bem-sucedido.

---

## **Pipeline CI/CD**
O GitHub Actions realiza:
1. **Build e Teste Automático:** Compilação da imagem Docker e execução dos testes.
2. **Versionamento Automático:** Incremento automático de versão baseado na última tag.
3. **Publicação no Docker Hub:** Publica a imagem com a tag gerada e a tag `latest`.

---

## **Melhorias Futuras**
- 🌟 Implementar autenticação mais robusta com OAuth.
- 📤 Integração com serviços externos via APIs RESTful.
- 🚀 Escalabilidade com Kubernetes.
- 📊 Dashboards adicionais no Grafana para maior visibilidade.

