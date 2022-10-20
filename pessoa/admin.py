from django.contrib import admin
from .models import Pessoa, Contato


@admin.action(description='Ativar todas as Pessoas.')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=True)

@admin.action(description='Desativar todas as Pessoas.')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)

class pessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa'
    ]
    list_filter = [
        'ativa',
        'data_nascimento',
    ]
    search_fields = [
        'nome_completo',
    ]
    actions = [
        ativar_todos,
        desativar_todos,
    ]


admin.site.register(Pessoa, pessoaAdmin)
admin.site.register(Contato)

