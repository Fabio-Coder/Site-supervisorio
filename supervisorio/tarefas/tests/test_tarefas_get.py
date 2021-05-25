from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest

from supervisorio.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_formulario_presente(resposta):
    assertContains(resposta, '<form')


def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')


@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(name='Tarefa 1', done=False),
        Tarefa(name='Tarefa 2', done=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def lista_de_tarefas_concluidas(db):
    tarefas_ok = [
        Tarefa(name='Tarefa 3', done=True),
        Tarefa(name='Tarefa 4', done=True),
    ]
    Tarefa.objects.bulk_create(tarefas_ok)
    return tarefas_ok


@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes, lista_de_tarefas_concluidas):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_lista_de_tarefa_pendentes_presente(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resposta_com_lista_de_tarefas, tarefa.name)


def test_lista_de_tarefa_concluidas_presente(resposta_com_lista_de_tarefas, lista_de_tarefas_concluidas):
    for tarefa_ok in lista_de_tarefas_concluidas:
        assertContains(resposta_com_lista_de_tarefas, tarefa_ok.name)
