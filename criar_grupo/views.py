from django.shortcuts import render
from .models import Grupo

# Create your views here.

def criar_grupo(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        grupo = Grupo(nome=nome, descricao=descricao)
        grupo.save()
        return render(request, 'grupo_criado.html', {'grupo': grupo})
    return render(request, 'criar_grupo.html')
