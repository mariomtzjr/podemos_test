from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Cuenta


# Register your models here.
class CuentaResource(resources.ModelResource):
    class Meta:
        model = Cuenta


@admin.register(Cuenta)
class CuentaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'grupo_id', 'estatus', 'monto', 'saldo', )
    ordering = ['id', ]
    resource_class = CuentaResource
