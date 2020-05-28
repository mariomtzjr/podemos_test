from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Grupo


# Register your models here.
class GrupoResource(resources.ModelResource):
    class Meta:
        model = Grupo


@admin.register(Grupo)
class GrupoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nombre', )
    ordering = ['id', ]
    resource_class = GrupoResource
