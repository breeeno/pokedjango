from rest_framework import viewsets
from tipo.api.serializer import ElementosSerializer
from tipo.models import Elemento


class ElementosViewSet(viewsets.ModelViewSet):
    queryset = Elemento.objects.all()
    serializer_class = ElementosSerializer
