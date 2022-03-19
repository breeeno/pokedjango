from rest_framework import viewsets
from tipo.api.serializer import TipoSerializer
from tipo.models import Tipo


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer