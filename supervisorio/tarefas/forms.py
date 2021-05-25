from django.forms import ModelForm

from supervisorio.tarefas.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['name']

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['name','done']