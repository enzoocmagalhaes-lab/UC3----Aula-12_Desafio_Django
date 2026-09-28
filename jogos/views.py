from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from .forms import JogoForm
from .models import Jogo

def home(request):
    return render(request, 'jogos/home.html', {'total_jogos': Jogo.objects.count()})

def listar_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/lista.html', {'jogos': jogos})

def detalhe_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    return render(request, 'jogos/detalhe.html', {'jogo': jogo})

@login_required
@require_http_methods(['GET', 'POST'])
def criar_jogo(request):
    form = JogoForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        jogo = form.save()
        messages.success(request, 'Jogo cadastrado com sucesso.')
        return redirect(jogo)
    return render(request, 'jogos/formulario.html', {'form': form, 'titulo_pagina': 'Adicionar jogo'})

@login_required
@require_http_methods(['GET', 'POST'])
def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    form = JogoForm(request.POST if request.method == 'POST' else None, instance=jogo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Jogo atualizado com sucesso.')
        return redirect(jogo)
    return render(request, 'jogos/formulario.html', {'form': form, 'jogo': jogo, 'titulo_pagina': 'Editar jogo'})

@login_required
@require_http_methods(['GET', 'POST'])
def excluir_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    # GET apenas mostra a confirmação; somente POST altera o banco.
    if request.method == 'POST':
        titulo = jogo.titulo
        jogo.delete()
        messages.success(request, f'Jogo "{titulo}" excluído com sucesso.')
        return redirect('jogos:lista')
    return render(request, 'jogos/confirmar_exclusao.html', {'jogo': jogo})
