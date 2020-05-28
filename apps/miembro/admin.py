from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Miembro


# Register your models here.
class MiembroResource(resources.ModelResource):
    class Meta:
        model = Miembro


@admin.register(Miembro)
class MiembroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('grupo_id', 'cliente_id')
    ordering = ['grupo_id', ]
    resource_class = MiembroResource
