# Gestão de Usuários

Esta é uma aplicação web para a gestão de clientes, construída com Flask e Peewee ORM.

## Requisitos

- Python 3.13+
- Flask
- Peewee
- Bootstrap 5

## Instalação do Python

Se você não tem o Python instalado, siga os passos abaixo:

1. Baixe o instalador do Python em [python.org](https://www.python.org/downloads/).
2. Execute o instalador e siga as instruções na tela.
3. Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/RiquelmiDev/G.Clientes.git
    cd G.Clientes
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Execução

1. Inicie a aplicação:
    ```bash
    python main.py
    ```

2. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:5000
    ```

## Estrutura do Projeto

- `main.py`: Arquivo principal para iniciar a aplicação.
- `configuration.py`: Configurações de rotas e banco de dados.
- `routes/`: Contém os blueprints para as rotas da aplicação.
- `database/`: Contém a configuração do banco de dados e os modelos.
- `templates/`: Contém os templates HTML.
- `static/`: Contém arquivos estáticos como CSS e JavaScript.

## Estrutura de Pastas

```
gestao-usuarios/
├── database/
│   ├── database.py
│   └── models/
│       └── cliente.py
├── routes/
│   ├── cliente.py
│   └── home.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── cru.js
├── templates/
│   ├── detalhe_cliente.html
│   ├── form_cliente.html
│   ├── index.html
│   ├── item_cliente.html
│   └── lista_clientes.html
├── .gitignore
├── configuration.py
├── main.py
├── README.md
└── requirements.txt
```

## Funcionalidades

- Adicionar, editar e deletar clientes.
- Visualizar detalhes dos clientes.
- Listar todos os clientes.

## Licença

Este projeto está licenciado sob a licença MIT.
