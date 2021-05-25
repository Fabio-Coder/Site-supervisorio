from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest

from supervisorio.tarefas.models import Tarefa


@pytest.fixture
def tarefa_pendente(db):
    return Tarefa.objects.create(name='Tarefa 1', done=False)


@pytest.fixture
def resposta_com_tarefa_pendente(client, tarefa_pendente):
    resp = client.post(
        reverse('tarefas:detalhe',
                kwargs={'tarefa_id': tarefa_pendente.id}),
        data={'done': 'true', 'name': f'{tarefa_pendente.name} - editada'}
    )
    return resp


def test_status_code(resposta_com_tarefa_pendente):
    assert resposta_com_tarefa_pendente.status_code == 302

def test_tarefa_feita(resposta_com_tarefa_pendente):
    assert Tarefa.objects.first().done





@pytest.fixture
def tarefa_concluida(db):
    return Tarefa.objects.create(name='Tarefa 1', done=True)


@pytest.fixture
def resposta_com_tarefa_concluida(client, tarefa_concluida):
    resp = client.post(
        reverse('tarefas:detalhe',
                kwargs={'tarefa_id': tarefa_concluida.id}),
        data={'name': f'{tarefa_concluida.name} - editada'}
    )
    return resp


def test_tarefa_pendente(resposta_com_tarefa_concluida):
    assert not Tarefa.objects.first().done