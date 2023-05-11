from django.shortcuts import render

from CadastroCliente.models import Cliente, Profissoes

# Create your views here.
def index (request):
    meu_nome = 'Ciclano da Silva'
    lista_frutas = ['Laranja', 'Maça', 'Banana']
    context = {

        'nome': meu_nome,
        'frutas': lista_frutas

    }
    return render(request, 'index.html', context)

def listar_cliente(request):
    #busca todos os clientes cadastrador na tabela 
    lista_clientes = Cliente.objects.all()
    # o dicionario (variavel) context é que vai mandar pro
    lista_profissoes = Profissoes.objects.all()
    context = {

        "clientes": lista_clientes,
        "profissoes": lista_profissoes
    }


    return render(request, 'lista_clientes.html', context)

def listar_profissoes(request):
    lista_profissoes = Profissoes.objects.all()
    context = {

        "profissoes": lista_profissoes
    }
    return render(request, 'lista_profissoes.html', context)

def detalhar_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    context = {
        "cliente" : cliente
    }
    return render (request, "cliente_detalhes.html", context)