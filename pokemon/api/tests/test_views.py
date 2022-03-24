import pytest
from django.shortcuts import resolve_url

from pokemon.models import Pokemon
from tipo.models import Tipo


@pytest.fixture
def fogo(db):
    return Tipo.objects.create(elemento='fogo')


def test_pokemon_create(rest_client, fogo: Tipo):
    data = {
        'nome': 'Pikachu',
        'elemento': [fogo.pk],
    }
    response = rest_client.post(resolve_url('pokemon-list'), data=data, format='json')

    assert response.status_code == 201
    assert Pokemon.objects.count() == 1
