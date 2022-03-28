from rest_framework.serializers import ModelSerializer
from tipo.models import Elemento


class ElementosSerializer(ModelSerializer):
    class Meta:
        model = Elemento
        fields = ['id', 'elemento']
