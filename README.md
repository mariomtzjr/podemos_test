# PODEMOS POGRESAR TEST

## Requerimientos
- Django==2.2.1
- django-import-export
- Python==3.7
- djangorestframework

### Funcionalidad Importar/Exportar datos desde el sitio de Administración
Se realizó mediante la biblioteca (django-import-export)[https://django-import-export.readthedocs.io/en/latest/].

#### Error al importar archivo data_calendariopagos.csv
- Error: "Enter a date/time date correct value".
- Solución: La columna fecha_pago tiene un formato de fecha *dd/mm/aaaa hh:mm*. Django tiene un formato para campos
DateTimeField default como *aaaa-mm-dd hh:mm:ss*. Por lo tanto para que no arrojara errores a la hora de importar
los datos, en el archivo data_calendariopagos.csv se cambió el formato de fecha_pago al formato de Django.
