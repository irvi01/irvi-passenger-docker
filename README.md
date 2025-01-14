# **Irvi Passenger Docker**

## **Descrição**
Este repositório contém uma imagem 🛊 Docker personalizada para executar aplicações 🔧 Python utilizando o Phusion Passenger como servidor de aplicação. O objetivo é criar um ambiente simples, flexível e escalável, ideal para aprendizado e exploração de conceitos de 📚 DevOps.

---

## **Funcionalidades**
- ✅ Suporte ao Passenger com 🔧 Python.
- ✅ Configuração baseada em 🇺🇸 Ubuntu 20.04.
- ✅ 📄 Dockerfile modular e extensível.
- ✅ Integração com 🔧 Flask para operações CRUD e autenticação JWT.
- ✅ Configuração de 📊 logs estruturados no formato JSON.
- ✅ 🏋️‍♂️ Testes automatizados integrados.
- ✅ Pipeline CI/CD para build, testes, versionamento automático e deploy.

---

## **Estrutura do Projeto**
```plaintext
irvi-passenger-docker/
├── app/
│   ├── __init__.py            # Configuração inicial do Flask e logs
│   ├── models.py              # Definição de modelos (ORM)
│   ├── routes.py              # Definição de rotas (CRUD e autenticação)
│   ├── requirements.txt       # Dependências da aplicação
│   ├── tests/                 # Testes automatizados
│   │   ├── __init__.py        # Inicialização dos testes
│   │   └── test_routes.py     # Testes das rotas
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline CI/CD
├── Dockerfile                 # Configuração da imagem Docker
├── main.py                    # Arquivo principal para inicializar a aplicação
├── passenger_wsgi.py          # Arquivo de integração com Passenger
└── README.md                  # Documentação do projeto
```

---

## **Configuração do Ambiente**

### **Requisitos**
- 🐋 Docker instalado.
- 🔗 Git configurado.

### **Clonar o Repositório**
```bash
git clone https://github.com/irvi01/irvi-passenger-docker.git
cd irvi-passenger-docker
```

---

## **Como Usar**

### **Build da Imagem Docker**
Para construir a imagem 🛊 Docker, execute:
```bash
docker build -t irvids/irvi-passenger-python .
```

### **Executar o Container**
Para rodar o 🛊 container, execute:
```bash
docker run -p 8080:80 irvids/irvi-passenger-python
```

Acesse a aplicação em [http://localhost:8080](http://localhost:8080).

---

## **Testes Automatizados**

### **Executar Testes Localmente**
1. Certifique-se de que todas as 🔧 dependências estão instaladas:
   ```bash
   pip install -r app/requirements.txt
   ```
2. Execute os 🏋️‍♂️ testes:
   ```bash
   pytest app/tests/
   ```

### **Executar Testes no Docker**
1. Certifique-se de que a imagem 🛊 Docker está atualizada.
2. Execute os testes diretamente no container:
   ```bash
   docker run --rm -e PYTHONPATH=/opt/app irvids/irvi-passenger-python pytest app/tests/
   ```

---

## **Rotas Disponíveis**

### **Autenticação**
- **POST /auth/register**: Registrar um novo usuário.
  - Body JSON:
    ```json
    {
      "username": "testuser",
      "password": "password123"
    }
    ```
- **POST /auth/login**: Realizar login e obter o token JWT.
  - Body JSON:
    ```json
    {
      "username": "testuser",
      "password": "password123"
    }
    ```

### **Operações com Itens**
- **GET /items**: Listar todos os itens (⛔️ requer autenticação).
- **GET /items/{id}**: Obter detalhes de um item específico (⛔️ requer autenticação).
- **POST /items**: Criar um novo item (⛔️ requer autenticação).
  - Body JSON:
    ```json
    {
      "name": "Novo Item"
    }
    ```
- **PUT /items/{id}**: Atualizar um item existente (⛔️ requer autenticação).
  - Body JSON:
    ```json
    {
      "name": "Item Atualizado"
    }
    ```
- **DELETE /items/{id}**: Deletar um item (⛔️ requer autenticação).

---

## **Pipeline CI/CD**
A pipeline do 🔧 GitHub Actions realiza:
1. **Build e Teste Automático**: Realiza o build da imagem Docker e executa os testes automatizados.
2. **Versionamento Automático**: Incrementa automaticamente a versão baseada na última tag.
3. **Deploy no 🛊 Docker Hub**: Publica a imagem Docker com a nova tag e como `latest`.

### **Configuração**
Certifique-se de configurar os seguintes segredos no repositório:
- `DOCKER_USERNAME`: Seu usuário no Docker Hub.
- `DOCKER_PASSWORD`: Sua senha ou token de acesso no Docker Hub.

---

## **Configuração de Logs**
Os 📊 logs são gerados no formato JSON para fácil integração com sistemas de monitoramento centralizados. Eles incluem informações como:
- Método HTTP e URL da requisição.
- Cabeçalhos e corpo da requisição.
- Timestamps detalhados.

---

## **Melhorias Futuras**
1. 🌟 Adicionar variáveis de ambiente para configurações dinâmicas.
2. 📊 Expandir o monitoramento e logs centralizados.
3. 🚀 Escalar a aplicação com balanceadores de carga.
4. 📈 Integrar observabilidade com Grafana e Prometheus.

Teste