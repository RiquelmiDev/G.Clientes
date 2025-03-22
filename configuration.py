from routes.home import home_route
from routes.cliente import cliente_route
from database.database import db
from database.models.cliente import Cliente

# executa todos os métodos de configuração da api
def configure_all(app):
    configure_routes(app)
    configure_db()

# configura as rotas da api
def configure_routes(app):
    # registra um blueprint na aplicação
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')#Todas as rotas dentro do blueprint cliente_route serão acessíveis com este prefixo /cliente.

# configura o banco de dados
def configure_db():
    db.connect() # conecta ao banco de dados
    db.create_tables([Cliente], safe=True) # cria as tabelas no banco de dados, se não existirem