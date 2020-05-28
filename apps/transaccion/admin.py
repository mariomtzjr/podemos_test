from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Transaccion


# Register your models here.
class TransaccionResource(resources.ModelResource):
    class Meta:
        model = Transaccion


@admin.register(Transaccion)
class TransaccionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'cuenta_id', 'fecha', 'monto', )
    ordering = ['id', ]
    resource_class = TransaccionResource
