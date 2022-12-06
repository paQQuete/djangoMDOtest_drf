import uuid

from django.db import models
from django.contrib.auth.models import User


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Entity(UUIDMixin, TimeStampedMixin):
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    value = models.IntegerField(blank=False, null=False)
    properties = models.ManyToManyField('Property', through='EntityProperty')

    def __str__(self):
        return f'{self.value}'


class Property(UUIDMixin, TimeStampedMixin):
    key = models.CharField(blank=False, null=False, max_length=255)
    value = models.CharField(blank=True, null=True, max_length=255)
    entities = models.ManyToManyField('Entity', through='EntityProperty')

    def __str__(self):
        return f'{self.key}:{self.value}'


class EntityProperty(UUIDMixin, TimeStampedMixin):
    entity_id = models.ForeignKey('Entity', on_delete=models.CASCADE)
    property_id = models.ForeignKey('Property', on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['entity_id', 'property_id'], name='entity_property_idx')]
