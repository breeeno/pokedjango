from rest_framework import viewsets
from pokemon.api.serializer import PokemonSerializer
from pokemon.models import Pokemon


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
