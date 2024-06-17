from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipamento

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == 'POST':
        id = request.POST['id']
        local = request.POST['local']
        Equipamento.objects.create(id=id, local=local)
        return redirect('lista_equipamentos')
    return render(request, 'cadastro.html')

def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'lista_equipamentos.html', {'equipamentos':equipamentos})