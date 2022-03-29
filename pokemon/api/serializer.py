from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from pokemon.models import Pokemon


class PokemonSerializer(ModelSerializer):
    elemento = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Pokemon
        fields = ['id', 'nome', 'elemento', 'sprite']
