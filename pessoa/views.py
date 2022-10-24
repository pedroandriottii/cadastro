from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Animal, Pessoa
from .forms import AnimalForm, PessoaForm

class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        #apenas encherga o usuário que cadastrou
        queryset = queryset.filter(usuario=self.request.user)
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
        return queryset

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'

def animais(request, pk_pessoa):
    animais = Animal.objects.filter(pessoa=pk_pessoa)
    return render(request, 'animal/animal_list.html', {'animais': animais, 'pk_pessoa': pk_pessoa})

def animaislist(request, pk_pessoa):
    animais = Animal.objects.all()
    return render(request, 'animal/animal_listtop.html', {'animais': animais, 'pk_pessoa': pk_pessoa}) 

def animal_novo(request, pk_pessoa):
    form = AnimalForm()
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.pessoa_id = pk_pessoa;
            animal.save()
            return redirect(reverse('pessoa.animais', args=[pk_pessoa]))
    return render(request, 'animal/animal_form.html', {'form': form})

def animal_editar(request, pk_pessoa, pk):
    animal = get_object_or_404(Animal, pk=pk)
    form = AnimalForm(instance=animal)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa.animais', args=[pk_pessoa]))
    return render(request, 'animal/animal_form.html', {'form': form})

def animal_remover(request, pk_pessoa, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal.delete()
    return redirect(reverse('pessoa.animais', args=[pk_pessoa]))