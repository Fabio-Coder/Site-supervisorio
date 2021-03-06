from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest
from supervisorio.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('tarefas:home'), data={'name': 'Tarefa'})
    return resp


def test_tarefa_existe_no_bd(resposta):
    assert Tarefa.objects.exists()


def test_redirect_depois_do_salvamento(resposta):
    assert resposta.status_code == 302


@pytest.fixture
def resposta_dado_invalido(client, db):
    resp = client.post(reverse('tarefas:home'), data={'name': ''})
    return resp


def test_tarefa_nao_existe_no_bd(resposta_dado_invalido):
    assert not Tarefa.objects.exists()


def test_erro_no_redirect_depois_do_salvamento(resposta_dado_invalido):
    assert resposta_dado_invalido.status_code == 400
