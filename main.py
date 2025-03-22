from flask import Flask
from configuration import configure_all

# inicializacao da API
app = Flask(__name__)

#configuracao da API
configure_all(app)

# execucao da API
app.run(debug=True)