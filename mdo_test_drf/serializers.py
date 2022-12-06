import re

from rest_framework import serializers

from .models import Entity, Property


class DynamicFieldsCategorySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class PropertySerializer(DynamicFieldsCategorySerializer):
    class Meta:
        model = Property
        fields = ('key', 'value')


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()
    properties = PropertySerializer(many=True, fields=['key', 'value'], read_only=True)

    def __init__(self, *args, **kwargs):
        data = kwargs.get('data')
        if data is not None:
            value = data.pop('data[value]')
            kwargs['data'].update({'value': value})
        super().__init__(*args, **kwargs)


    class Meta:
        model = Entity
        fields = ('value', 'properties')
