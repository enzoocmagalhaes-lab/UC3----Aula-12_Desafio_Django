from django.urls import path
from . import views

app_name = 'jogos'
urlpatterns = [
    path('', views.home, name='home'),
    path('jogos/', views.listar_jogos, name='lista'),
    path('jogos/novo/', views.criar_jogo, name='criar'),
    path('jogos/<int:pk>/', views.detalhe_jogo, name='detalhe'),
    path('jogos/<int:pk>/editar/', views.editar_jogo, name='editar'),
    path('jogos/<int:pk>/excluir/', views.excluir_jogo, name='excluir'),
]
