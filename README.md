
# 🚀 Python vs MongoDB Atlas

## 
✨ Sobre o Projeto

Este projeto é um exemplo de API RESTful construída com **FastAPI** para operações CRUD (Create, Read, Update, Delete) em um banco de dados **MongoDB**. Utiliza o **Pymongo** como driver para a comunicação com o MongoDB e o **Uvicorn** como servidor web assíncrono. As configurações sensíveis, como a string de conexão do banco de dados, são gerenciadas de forma segura com `python-dotenv`.

É uma solução leve e performática para construir APIs modernas em Python.

## 
🛠️ Tecnologias

As seguintes tecnologias foram usadas na construção deste projeto:

  * **FastAPI**: Um framework web moderno e rápido para construir APIs com Python 3.7+ baseado em tipagem padrão Python.
  * **Uvicorn**: Um servidor ASGI de alta performance, usado para rodar a aplicação FastAPI.
  * **Pymongo**: O driver Python oficial e recomendado para MongoDB.
  * **python-dotenv**: Uma biblioteca para carregar variáveis de ambiente de um arquivo `.env`.
  * **Python 3.x**

-----

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter o Python 3.x instalado em sua máquina. Além disso, você precisará de uma instância do MongoDB acessível (local ou em nuvem, como o MongoDB Atlas).

-----

## 🚀 Instalação e Execução

Siga os passos abaixo para configurar e rodar o projeto localmente:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/SeuUsuario/NomeDoSeuRepositorio.git
    cd NomeDoSeuRepositorio
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**

      * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
      * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Certifique-se de ter um arquivo `requirements.txt` com as dependências listadas: `fastapi`, `uvicorn`, `pymongo`, `python-dotenv`)*

5.  **Crie o arquivo `.env`:**
    Crie um arquivo chamado `.env` na raiz do projeto com as suas variáveis de ambiente. Veja a seção [Variáveis de Ambiente](https://www.google.com/search?q=%23-vari%C3%A1veis-de-ambiente) para mais detalhes.

    Exemplo de `.env`:

    ```
    MONGO_DB_URL="mongodb://localhost:27017/"
    MONGO_DB_NAME="nome_do_seu_banco"
    ```

    Ou para MongoDB Atlas:

    ```
    MONGO_DB_URL="mongodb+srv://<user>:<password>@<cluster-url>/<db-name>?retryWrites=true&w=majority"
    MONGO_DB_NAME="nome_do_seu_banco"
    ```

6.  **Execute a aplicação:**

    ```bash
    uvicorn app.main:app --reload
    ```

    O `--reload` é útil durante o desenvolvimento para que o servidor reinicie automaticamente ao detectar mudanças no código.

7.  **Acesse a API:**
    A API estará disponível em `http://127.0.0.1:8000`.
    Você pode acessar a documentação interativa (Swagger UI) em `http://127.0.0.1:8000/docs`.
    Ou a documentação ReDoc em `http://127.0.0.1:8000/redoc`.

-----

## 📁 Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
.
├── app/
│   ├── __init__.py
│   ├── main.py             # Ponto de entrada da aplicação FastAPI
│   ├── controllers/        # Contém a lógica de negócio e as operações CRUD
│   │   ├── __init__.py
│   │   └── (seus_controllers).py
│   ├── database/           # Configuração de conexão com o MongoDB
│   │   ├── __init__.py
│   │   └── connection.py
│   ├── models/             # Modelos de dados (Pydantic) e schemas
│   │   ├── __init__.py
│   │   └── user_model.py   # Exemplo: modelo de usuário
│   └── routes/             # Definição das rotas da API
│       ├── __init__.py
│       └── (suas_rotas).py
├── .env                    # Variáveis de ambiente (ex: string de conexão do DB)
├── .gitignore              # Arquivos e diretórios a serem ignorados pelo Git
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

-----

## 📡 Endpoints da API

A documentação interativa da API (Swagger UI) está disponível em `http://127.0.0.1:8000/docs`, onde você pode testar todos os endpoints.

Exemplo de endpoints comuns (ajuste conforme seu projeto):

  * **GET /users**: Lista todos os usuários.
  * **GET /users/{id}**: Retorna um usuário específico pelo ID.
  * **POST /users**: Cria um novo usuário.
  * **PUT /users/{id}**: Atualiza um usuário existente.
  * **DELETE /users/{id}**: Exclui um usuário.

-----

## 🔒 Variáveis de Ambiente

O projeto utiliza o pacote `python-dotenv` para carregar variáveis de ambiente do arquivo `.env`. Este arquivo **NÃO** deve ser versionado no Git por conter informações sensíveis.

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

  * `MONGO_DB_URL`: A string de conexão URI para o seu banco de dados MongoDB.
      * Ex: `mongodb://localhost:27017/` (para um MongoDB local)
      * Ex: `mongodb+srv://<user>:<password>@<cluster-url>/<db-name>?retryWrites=true&w=majority` (para MongoDB Atlas)
  * `MONGO_DB_NAME`: O nome do banco de dados MongoDB que a aplicação irá utilizar.

