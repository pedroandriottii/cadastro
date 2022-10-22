from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaPessoaView.as_view()), name='pessoa.index'),
    path('novo/', login_required(PessoaCreateView.as_view()), name='pessoa.novo'),
    path('<int:pk>/editar', login_required(PessoaUpdateView.as_view()), name='pessoa.editar'),
    path('<int:pk>/remover', login_required(PessoaDeleteView.as_view()), name='pessoa.remover'), 
    path('<int:pk_pessoa>/animais', login_required(views.animais), name='pessoa.animais'),
    path('<int:pk_pessoa>/animal/novo/', login_required(views.animal_novo), name='animal.novo'),
    path('<int:pk_pessoa>/animal/<int:pk>/editar', login_required(views.animal_editar), name='animal.editar'),
    path('<int:pk_pessoa>/animal/<int:pk>/remover', login_required(views.animal_remover), name='animal.remover'),  
]
