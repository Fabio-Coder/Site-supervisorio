from urllib.request import HTTPRedirectHandler

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

# Create your views here.
from supervisorio.tarefas.forms import TarefaNovaForm
from supervisorio.tarefas.models import Tarefa


def home(request):
    tarefas_pendentes = Tarefa.objects.filter(done=False).all()
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes': tarefas_pendentes},
                          status=400)
    return render(request, 'tarefas/home.html', {'tarefas_pendentes': tarefas_pendentes})
