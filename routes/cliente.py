from flask import Blueprint,render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ Lista todos os clientes """

    #busca todos os clientes no banco de dados
    clientes = Cliente.select()

    return render_template('lista_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Recebe os dados do cliente e insere no banco de dados """
    data = request.json

    novo_usuario = Cliente.create(
        nome=data['nome'], 
        email=data['email'],
    )

    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    """ Renderiza o formulario de cadastro de cliente """
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>') 
#recebe o id do cliente como um parametro do tipo inteiro da rota e passa para o metodo detalhe_cliente
def detalhe_cliente(cliente_id):
    """ Obtem um cliente pelo id """

    #busca o cliente no db pelo id
    cliente = Cliente.get_by_id(cliente_id) 

    return render_template('detalhe_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit') 
def form_edit_cliente(cliente_id):
    """ Renderiza o formulario de edicao de cliente """
    
    #busca o cliente no db pelo id
    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT']) 
def atualizar_cliente(cliente_id):
    """ Atualiza um cliente pelo id """
    # obtem os dados do formulario de edicao
    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)

    #edita o cliente
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    #salva as alteracoes
    cliente_editado.save()

    # editar usuario

    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE']) 
def deletar_cliente(cliente_id):
    """ Deletar um cliente pelo id """

    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return 'Cliente deletado com sucesso', 204