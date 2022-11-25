# CNAB Table_APP

### Sobre o aplicativo e sua funcionalidade:
- Este app foi desenvolvido para converter padrões CNAB em tabelas armazenando os dados em uma database
- **Os padrões CNAB devem ser fornecidos pelo usuário em um arquivo .txt**
- Neste projeto existe um arquivo **exemplo_CNAB.txt** que exemplifica o padrão a ser seguido.
- Caso o arquivo .txt passado esteja fora do padrão proposto ocorrerá um erro.

## Tecnologias Utilizadas:
- Python 3
- Django Framework
- Docker
- SQLite 3

## Endpoints:
- Para fazer upload do arquivo: (http://localhost:8000)
- Para acessar as tabelas com os dados da DB: (http://localhost:8000/transactions/)

## Instalação (Utilizando Docker):
- Clone este repositório em seu ambiente local
- Crie um arquivo `.env` baseando-se no arquivo **`.env.example`**
- Rode o comando **`docker-compose up --build`** e aguarde a finalização da configuração
- Agora a aplicação estará rodando neste link: (http://localhost:8000)
- Caso queira acessar apenas as tabelas com as transações já contidas na database acesse (http://localhost:8000/transactions/)

## Instalação sem docker (local):
- Clone este repositório em seu ambiente local
- Crie um arquivo `.env` baseando-se no arquivo **`.env.example`**
- Adicione um ambiente virtual **`python -m venv venv`** na pasta do projeto
- Ative o ambiente virtual criado || **Linux:`source ./venv/bin/activate` || Windows:`./venv/Scripts/activate`**
- Rode o comando **`pip install -r requirements.txt`** para instalar as dependências
- Implemente as migrações através dos comandos **`python manage.py makemigrations`**
- Crie a database utilizando o comando **`python manage.py migrate`**
- Com as migrações em ordem podemos rodar **`python manage.py runserver`**
- Agora a aplicação deve estar rodando neste link: (http://localhost:8000)
- Caso queira acessar apenas as tabelas com as transações já contidas na database acesse: (http://localhost:8000/transactions/)
