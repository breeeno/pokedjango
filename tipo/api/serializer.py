from rest_framework.serializers import ModelSerializer
from tipo.models import Tipo


class TipoSerializer(ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'elemento']
