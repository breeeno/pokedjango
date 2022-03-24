from rest_framework.serializers import ModelSerializer
from tipo.models import Elementos


class ElementosSerializer(ModelSerializer):
    class Meta:
        model = Elementos
        fields = ['id', 'elemento']
