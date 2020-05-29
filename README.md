# PODEMOS POGRESAR TEST

## Requerimientos
- Django==2.2.1
- django-import-export
- Python==3.7
- djangorestframework

### Importar/Exportar datos desde el sitio de Administración
(django-import-export)[https://django-import-export.readthedocs.io/en/latest/].

##### Error al importar archivo data_calendariopagos.csv
- Error: "Enter a date/time date correct value".
- Solución: La columna fecha_pago tiene un formato de fecha *dd/mm/aaaa hh:mm*. Django tiene un formato para campos
DateTimeField default como *aaaa-mm-dd hh:mm:ss*. Por lo tanto para que no arrojara errores a la hora de importar
los datos, en el archivo data_calendariopagos.csv se cambió el formato de fecha_pago al formato de Django.

### Endpoints
- /api/calendario-pago/<cuenta_id>/listar/: Lista el caledario de pagos de una cuenta en particular.
- /api/clientes/listar/: Listado de todos los clientes.
- /api/clientes/editar/<id_cliente>: Edita información de un cliente en particular.
- /api/grupos/listar/: Listado de los grupos existentes, los miembros que se encuentran en dicho grupo, son un listado de clientes.
- /api/grupos/eliminar/<id_grupo>: Eliminar el grupo con id <id_grupo>
- /api/miembros/crear/: Añade un cliente a un grupo en particular.
- /api/miembros/listar/: Listado de los grupos y clientes (conforman la relación de miembro).
- /api/miembros/editar/<id_miembro>: Edita el objeto miembro en cuestión. El <id_miembro> debe ser en donde se encuentra el cliente o el grupo que se desea modificar.
- /api/miembros/eliminar/<id_miembro>: Elimina cliente que se encuentra en un grupo particular.
- /api/cuentas/listar/: Listado de las cuentas pertenecimientes a un grupo, así como el calendario de pagos ligadas a una cuenta.
