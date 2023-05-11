from django.urls import path
from CadastroCliente import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes', views.listar_cliente, name='clientes'),
    path('profissoes', views.listar_profissoes, name='profissoes'),
    path('cliente/<int:id>', views.detalhar_cliente, name='detalhar')

]