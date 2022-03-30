from rest_framework import viewsets
from pokemon.api.serializer import PokemonSerializer
from pokemon.models import Pokemon
from rest_framework import filters


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']