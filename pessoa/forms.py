from django import forms
from .models import Pessoa, Animal

class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento']

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'tipo', 'vacina', 'descricao']
         
