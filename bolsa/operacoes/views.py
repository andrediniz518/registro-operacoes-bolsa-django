from django.shortcuts import render
from django.http import HttpResponse
from .models import Operacao
from .forms import OperacaoForm
from django.shortcuts import redirect



# Create your views here.

def home(request):
    operacoes = Operacao.objects.all()
    contexto = {
        "titulo": "Sistema de Registro de Operações",
        "mensagem": "Bem vindo ao Sistema!",
        "operacoes": operacoes,
    }
    return render(request, "operacoes/home.html", contexto)


def nova_operacao(request):
    if request.method == "POST":
        form = OperacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OperacaoForm()
    return render(
        request,
        "operacoes/nova_operacao.html",
        {'form': form},
    )
        
def editar_operacao(request, id):
    operacao = Operacao.objects.get(id=id)
    if request.method == "POST":
        form = OperacaoForm(request.POST, instance=operacao)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OperacaoForm(instance=operacao)

    return render(
        request, 'operacoes/editar_operacao.html',
        {'form': form},

    )


def excluir_operacao(request, id):
    operacao = Operacao.objects.get(id=id)

    if request.method == 'POST':
        operacao.delete()
        return redirect('home')
    return render(
        request,
        'operacoes/excluir_operacao.html',
        {'operacao': operacao},

    )