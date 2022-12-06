from rest_framework import viewsets

from .serializers import EntitySerializer, PropertySerializer
from .models import Entity, Property


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all().order_by('value')
    serializer_class = EntitySerializer

    def perform_create(self, serializer):
        serializer.save(modified_by=self.request.user)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('key')
    serializer_class = PropertySerializer
