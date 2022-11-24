# CNAB Table_APP

### **Este app foi desenvolvido para converter padrões CNAB em tabelas através de um arquivo .txt que deve ser fornecido pelo usuário.

## Tecnologias Utilizadas:
- Python 3
- Django Framework
- Docker
- SQLite 3

## Instalação (Utilizando Docker):
- Clone este repositório em seu ambiente local.
- Adicione um ambiente virtual **`python -m venv venv`** na pasta do projeto.
- Rode o comando **`docker-compose up --build`** e aguarde a finalização da configuração.
- Agora a aplicação deve estar rodando neste link: (http://localhost:8000)
- Caso queira acessar apenas as tabelas com as transações já contidas na database acesse (http://localhost:8000/transactions/)

## Instalação sem docker (local):
- Clone este repositório em seu ambiente local.
- Adicione um ambiente virtual **`python -m venv venv`** na pasta do projeto.
- Rode o comando **`pip install -r requirements.txt`** oara instalar as dependências.
- Implemente as migrações através dos comandos **`python manage.py makemigrations`**
- Crie a database utilizando o comando **`python manage.py migrate`**
- Com as migrações em ordem podemos rodar **`python manage.py runserver`**
- Agora a aplicação deve estar rodando neste link: (http://localhost:8000)
- Caso queira acessar apenas as tabelas com as transações já contidas na database acesse: (http://localhost:8000/transactions/)