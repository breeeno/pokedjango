import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def rest_client():
    return APIClient()


@pytest.fixture
def usuario_logado(db, django_user_model, rest_client):
    usuario_logado = baker.make(django_user_model, first_name='Beltrano')
    return usuario_logado


@pytest.fixture
def client_com_usuario_logado(usuario_logado, rest_client):
    rest_client.force_login(usuario_logado)
    return rest_client
