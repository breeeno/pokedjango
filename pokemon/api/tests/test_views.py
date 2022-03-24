import pytest
from django.shortcuts import resolve_url
from pokemon.models import Pokemon
from tipo.models import Elemento


@pytest.fixture
def grama(db):
    return Elemento.objects.create(nome='grama')


@pytest.fixture
def pokemon(db, grama):
    p = Pokemon.objects.create(nome='bulbasaur')
    p.elemento.add(grama)
    return p


@pytest.fixture
def pokemon_new(db, rest_client):
    pokemon_new = rest_client.patch('pokemon-detail', {'nome': 'voador'}, format='json')
    return pokemon_new


def test_pokemon_create(rest_client, grama: Elemento):
    data = {
        'nome': 'Bulbasaur',
        'elemento': [grama.pk],
    }
    response = rest_client.post(resolve_url('pokemon-list'), data=data, format='json')

    assert response.status_code == 201
    assert Pokemon.objects.count() == 1


def test_pokemon_delete(rest_client, pokemon: Pokemon, grama: Elemento):
    data = {
        'nome': [pokemon.pk],
        'elemento': [grama.pk],
    }
    response = rest_client.delete(resolve_url('pokemon-detail',
                                  pk=pokemon.pk),
                                  data=data,
                                  format='json')
    assert response.status_code == 204


def test_pokemon_get(rest_client, pokemon):
    response = rest_client.get(resolve_url('pokemon-list'),
                               pokemon=pokemon,
                               grama=grama,
                               format='json')
    assert response.status_code == 200


def test_pokemon_patch(rest_client, pokemon_new):
    response = rest_client.get(resolve_url('pokemon-list'),
                               pokemon_new=pokemon_new,
                               format='json')
    assert response.status_code == 200
