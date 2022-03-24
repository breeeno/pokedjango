import pytest
from django.shortcuts import resolve_url
from pokemon.models import Pokemon
from tipo.models import Elementos


@pytest.fixture
def fogo(db):
    return Elementos.objects.create(elemento='fogo')


def test_pokemon_create(rest_client, fogo: Elementos):
    data = {
        'nome': 'Pikachu',
        'elemento': [fogo.pk],
    }
    response = rest_client.post(resolve_url('pokemon-list'), data=data, format='json')

    assert response.status_code == 201
    assert Pokemon.objects.count() == 1


def test_pokemon_delete(rest_client, fogo: Elementos):
    data = {
        'nome': 'Pikachu',
        'elemento': [fogo.pk],
    }
    response = rest_client.delete(resolve_url('pokemon/1/'), data=data, format='json')

    assert response.status_code == 404
    assert Pokemon.objects.count() == 0


@pytest.fixture
def pkm(db, rest_client):
    pkm = rest_client.post('pokemon-list',
                           {'nome': 'Charmander',
                            'elemento': 'fogo'},
                           format='json')
    return pkm


def test_pokemon_get(rest_client, pkm):
    response = rest_client.get(resolve_url('pokemon-list'), pkm=pkm, format='json')
    assert response.status_code == 200


@pytest.fixture
def pkm_new(db, rest_client):
    pkm_new = rest_client.patch(resolve_url('pokemon/1/'), {'elemento': 'voador'}, format='json')
    return pkm_new


def test_pokemon_patch(rest_client, pkm_new):
    response = rest_client.get(resolve_url('pokemon-list'), pkm_new=pkm_new, format='json')
    assert response.status_code == 200
