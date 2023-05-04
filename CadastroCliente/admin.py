from django.contrib import admin
from CadastroCliente.models import Cliente, Profissoes, Telefone, Interesse
# Register your models here.
# Classe para exibir Telefones no cad. de cliente
class Telefones(admin.StackedInline):
    model = Telefone
    extra = 1


class ClienteAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome', 'cidade']
    list_display_links = ['id', 'nome']
    list_filter = ['bairro', 'cidade', 'Ativo']
    search_fields = ['nome']
    inlines = [Telefones]

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Profissoes)
admin.site.register(Telefone)
admin.site.register(Interesse)