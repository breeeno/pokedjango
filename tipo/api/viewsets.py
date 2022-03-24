from rest_framework import viewsets
from tipo.api.serializer import ElementosSerializer
from tipo.models import Elementos


class ElementosViewSet(viewsets.ModelViewSet):
    queryset = Elementos.objects.all()
    serializer_class = ElementosSerializer
