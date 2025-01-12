# **Irvi Passenger Docker**

## **Descrição**
Este repositório contém uma imagem Docker personalizada para executar aplicações Python utilizando o Phusion Passenger como servidor de aplicação. O objetivo é criar um ambiente simples, flexível e escalável, ideal para aprendizado.

---

## **Funcionalidades**
- ✅ Suporte ao Passenger com Python.
- ✅ Configuração baseada em Ubuntu 20.04.
- ✅ Dockerfile modular e extensível.
- ✅ Pronto para uso com Flask e outras aplicações Python.

---

## **Estrutura do Projeto**
```plaintext
irvi-passenger-docker/
├── app/
│   ├── __init__.py            # Configuração inicial do Flask
│   ├── models.py              # Definição de modelos (ORM)
│   ├── routes.py              # Definição de rotas
│   ├── requirements.txt       # Dependências da aplicação
│   ├── tests/                 # Testes automatizados
│   │   ├── __init__.py        # Inicialização dos testes
│   │   └── test_routes.py     # Testes das rotas
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
Para construir a imagem Docker, execute:
```bash
docker build -t irvi-passenger-python .
```

### **Executar o Container**
Para rodar o container, execute:
```bash
docker run -p 8080:80 irvi-passenger-python
```

Acesse a aplicação em [http://localhost:8080](http://localhost:8080).

---

## **Testes Automatizados**

### **Executar Testes Localmente**
1. Certifique-se de que todas as dependências estão instaladas:
   ```bash
   pip install -r app/requirements.txt
   ```

2. Execute os testes:
   ```bash
   pytest app/tests/
   ```

### **Executar Testes no Docker**
1. Certifique-se de que a imagem Docker está atualizada.
2. Execute os testes diretamente no container:
   ```bash
   docker run --rm irvi-passenger-python pytest app/tests/
   ```

---

## **Configuração do Dockerfile**
O `Dockerfile` foi projetado para:
1. 📦 Instalar o Passenger e dependências do Python.
2. 🔧 Configurar o ambiente para rodar aplicações Python.
3. 📂 Copiar e configurar a aplicação Python.

---

## **Melhorias Futuras**
1. 🌟 Adicionar variáveis de ambiente para configurações dinâmicas.
2. 📤 Publicar a imagem no Docker Hub.
3. 🚀 Expandir a aplicação Flask com mais funcionalidades.
4. 📊 Configurar logs e monitoramento para o Passenger.

