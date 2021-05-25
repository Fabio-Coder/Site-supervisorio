from urllib.request import HTTPRedirectHandler

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

# Create your views here.
from supervisorio.tarefas.forms import TarefaNovaForm, TarefaForm
from supervisorio.tarefas.models import Tarefa


def home(request):
    tarefas_pendentes = Tarefa.objects.filter(done=False).all()
    tarefas_concluidas = Tarefa.objects.filter(done=True).all()
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(
                request, 'tarefas/home.html', {
                    'form': form,
                    'tarefas_pendentes': tarefas_pendentes,
                    'tarefas_concluidas': tarefas_concluidas
                }, status=400)
    return render(
        request, 'tarefas/home.html', {
            'tarefas_pendentes': tarefas_pendentes,
            'tarefas_concluidas': tarefas_concluidas})


def detalhe(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST, instance=tarefa)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))
