from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Cliente


# Register your models here.
class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente


@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nombre', )
    ordering = ['id', ]
    resource_class = ClienteResource
