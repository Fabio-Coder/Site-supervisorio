import pytest as pytest
from django.urls import reverse

from supervisorio.tarefas.models import Tarefa


@pytest.fixture
def tarefa(db):
    return Tarefa.objects.create(name='Tarefa 10', done=True)


@pytest.fixture
def resposta(client, tarefa):
    return client.post(reverse('tarefas:delete'))

    def test_apagar_tarefa(resposta):

        assert not Tarefa.objects.exists()
