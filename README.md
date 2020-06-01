# PODEMOS POGRESAR TEST

## Requerimientos
- Django==2.2.10
- django-import-export
- Python==3.7
- djangorestframework

### Instalación de requerimientos  
Para instalar Python, puede realizarse desde su [página oficial](https://www.python.org/downloads/release/python-370/). Debe de estar instalando Python para poder ejecutar los comandos siguientes.  
`pip install django==2.2.1`  
`pip install djandorestframework`  
`pip install django-import-export`  
ó  
`pip install -r requirements.txt`

Para ejecutar el comando `pip install -r requirements.txt` es necesario estar situado en el directorio que contiene el archivo txt.

### Set up del proyecto
El proyecto puede levantarse ejecutando el siguiente comando:    
`python manage.py runserver`  
El servidor comenzará a levantar y si no hay errores, debemos obtener una salida como la siguiente:  
```
System check identified no issues (0 silenced).
June 01, 2020 - 15:45:23
Django version 2.2.10, using settings 'app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

El proyecto tiene un archivo llamado *db.sqlite3*, que es el archivo que contiene nuestra base de datos por default en un proyecto django (motor SQLite), por lo tanto, no es necesario ejecutar el comando `python manage.py migrate`, ya que este comando crea las tablas de nuestros modelos y las que django trae por default.  

El sitio de administración se encuentra habilitado en la url *localhost://8000/admin*, existe un super usuario *eval*, con password *password*.


### Importar/Exportar datos desde el sitio de Administración
Para importar los datos proporcionados para el proyecto, se utilizó la biblioteca django-import-export:  
[django-import-export](https://django-import-export.readthedocs.io/en/latest/api_admin.html).

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
- /api/cuentas/crear/: Crea una cuenta. Automáticamente se genera su calendario de Pagos con los datos (monto) introducidos.
- /api/transacciones/crear/: Crear una transacción (realizar pago a una cuenta).

### Validaciones adicionales
- Al crear el calendario de pagos se valida que el día de pago sea únicamente día hábil.
- Cuando una transacción se crea de manera correcta se actualiza el saldo de la cuenta. NOTA: No se especifica validación de num_pago para cada pago realizado a una cuenta, por lo que el sistema únicamente ve el pago 1. Tampoco se especifica la validación para num_pago con respecto a fecha_pago.
- Si el monto de una transacción es mayor al pago que debe ser, la transacción se rechaza.
