# PODEMOS POGRESAR TEST

## Requerimientos
- Django==2.2.10
- django-import-export
- Python==3.7
- djangorestframework

### Instalación de requerimientos  
Para instalar Python, puede realizarse desde su [página oficial](https://www.python.org/downloads/release/python-370/). Debe de estar instalando Python para poder ejecutar los comandos siguientes.  
`pip install django==2.2.10`  
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

### Probar funcionalidades
Para hacer uso del sistema, cada endpoint, representa la url que nos lleva a dicha funcionalidad. Por ejemplo para ser el listado de todos los clientes, basta con colocar en la url de un navegador el siguiente valor:

#### Listar clientes
url: `localhost:8000/api/clientes/listar/`

#### Editar un cliente existente
url: `localhost:8000/api/clientes/editar/<id_cliente>`  
El id de cliente puede obtenerse a través de la funcionalidad *Listar clientes* con el campo **id**.

#### Listar grupos
url: `localhost:8000/api/grupos/listar/`

#### Eliminar un grupo
url: `localhost:8000/api/grupos/eliminar/<id_grupo>`  
El id de grupo puede obtenerse a través de la funcionalidad *Listar grupos*, con el campo **id**.

#### Añadir un cliente a un grupo existente
url: `localhost:8000/api/miembros/crear/`  
El campo **Grupo Id** será el grupo al que queramos integrar el cliente con valor en el campo **Cliente Id**. Una vez establecidos estos dos valores, presionar el botón **POST**.

#### Listar miembros
url: `localhost:8000/api/miembros/listar/`  
La información obtenida para esta url es como la siguiente:  
```
{
        "id": 1,
        "grupo_id": "XYZW1",
        "cliente_id": "MNOPQ01"
},
{
        "id": 11,
        "grupo_id": "GHIJK",
        "cliente_id": "NMZXC11"
 }
```
El valor del campo **id** corresponde al id del registro de la tabla miembro. Este *id* nos será útil cuando queramos reasignar un cliente a un grupo diferente del que pertenece. Esta salida de información nos dice que el cliente **MNOPQ01** pertenece al grupo **XYZW1** y que el cliente **NMZXC11** pertenece al grupo **GHIJK**.

#### Editar grupos
url: `localhost:8000/api/miembros/editar/<id_miembro>`  
El valor de *<id_miembro>* es un valor que podemos obtener con la url de *Listar miembros*. Suponiendo que ahora el cliente **NMZXC11** ya no estará en el grupo **GHIJK** y ahora formará parte del grupo **XYZW1**, el valor *<id_miembro>* que debemos colocar en la URL para reasignarlo de grupo es el **id=11**, por lo tanto, la url quedaría de la siguiente manera `localhost:8000/api/miembros/editar/11`.  
La salida que obtendremos es la siguiente: 
```
{
    "serializer": {
        "id": 11,
        "grupo_id": "GHIJK",
        "cliente_id": "NMZXC11"
    }
}
```
Para reasignar al cliente **NMZXC11** al grupo **XYZW1**, lo primero que debemos hacer seleccionar en el campo **Cliente Id** el valor del cliente, el cual sería **NMZXC11**, y el valor del campo **Grupo Id** debe de ser al grupo al cual queremos cambiarlo, en este caso sería **Grupo Id = XYZW1**. Al finalizar, presionamos el botón **POST**.

Automaticamente, después de presionar el botón **POST**, la información que veremos es el resultado de haber colocado en la url del navegador lo siguiente `localhost:8000/api/miembros/listar`. Si volvemos a observar el id del miembro 11, podemos observar que nuestro clinete **NMZXC11**, ahora forma parte del grupo **XYZW1**, al igual que el cliente **MNOPQ1**.
```
{
        "id": 1,
        "grupo_id": "XYZW1",
        "cliente_id": "MNOPQ01"
},
{
        "id": 11,
        "grupo_id": "XYZW1",
        "cliente_id": "NMZXC11"
}
```
#### Eliminar un cliente de un grupo en particular
url: `localhost:8000/api/miembros/eliminar/<id_miembro>`  
Para esta funcionalidad, el valor de *<id_miembro>* tiene el mismo concepto que en *Editar grupos*. Por ejemplo, si quisiéramos que el cliente **NMZXC11** ya no formara parte de ningún grupo, incluyendo al que pertenece actualmente, la url para hacerlo sería `localhost:8000/api/miembros/eliminar/11`.
Para eliminar a dicho cliente podemos presionar directamente el botón de color rojo **DELETE** y confirmamos la eliminación del cliente en ese grupo, o presionamos el botón **POST** y seleccionamos en el campo **Grupo Id** el valor de **XYZW1** y en el campo **Cliente Id** el valor de **NMZXC11**, y presionar el botón **POST**. En ambos casos, la salida de información será el listado de miembros, en donde podemos ver que el id más grande es 10, ya que el 11 correspondía al cliente **NMZXC11** que se encontraba en el grupo **XYZW1**.


### Validaciones adicionales
- Al crear el calendario de pagos se valida que el día de pago sea únicamente día hábil.
- Cuando una transacción se crea de manera correcta se actualiza el saldo de la cuenta. NOTA: No se especifica validación de num_pago para cada pago realizado a una cuenta, por lo que el sistema únicamente ve el pago 1. Tampoco se especifica la validación para num_pago con respecto a fecha_pago.
- Si el monto de una transacción es mayor al pago que debe ser, la transacción se rechaza.
