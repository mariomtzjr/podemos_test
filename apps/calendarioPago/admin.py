from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import CalendarioPago


# Register your models here.
class CalendarioPagoResource(resources.ModelResource):
    class Meta:
        model = CalendarioPago


@admin.register(CalendarioPago)
class CalendarioPagoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cuenta_id', 'num_pago', 'monto', 'fecha_pago', 'estatus')
    ordering = ['cuenta_id', 'id']
    resource_class = CalendarioPagoResource
