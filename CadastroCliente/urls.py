from django.urls import path
from CadastroCliente import views

urlpatterns = [
    path('', views.index, name='index'),
]