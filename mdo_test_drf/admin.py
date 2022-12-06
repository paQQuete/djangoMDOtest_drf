from django.contrib import admin
from .models import Entity, Property, EntityProperty



class EntityPropertyInline(admin.TabularInline):
    model = EntityProperty
    autocomplete_fields = ['entity_id']

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    inlines = (EntityPropertyInline, )
    list_display = ('modified_by', 'value')
    search_fields = ['properties']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    search_fields = ['properties']