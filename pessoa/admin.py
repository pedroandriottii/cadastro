from django.contrib import admin
from .models import Animal, Pessoa


class pessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
    ]
    list_filter = [
        'data_nascimento',
    ]
    search_fields = [
        'nome_completo',
    ]

admin.site.register(Pessoa, pessoaAdmin)
admin.site.register(Animal)

