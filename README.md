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
También podemos seleccionar de nuestro menú de navegación la pestaña **Clientes** desde cualquier otra url y posteriormente **Listar**. Obtendremos una tabla con el listado de todos los clientes registrados.

#### Editar un cliente existente  
Para editar un cliente, sólo basta con dar click en el enlace **Editar** de la columna *Acciones* sobre la fila en donde se encuentra el nombre del cliente a editar. En la vista posterior se deberá modificar la información pertinente, al finalizar se deberá presionar el botón *Guardar*. Si por equivocación se presiona el enlace **Editar**, basta con presionar el botón *Cancelar* para regresar al listado de clientes.

#### Listar grupos
url: `localhost:8000/api/grupos/listar/`  
También podemos seleccionar de nuestro menú de navegación la pestaña **Grupos** desde cualquier otra url y posteriormente **Listar**. Se mostrará una tabla en la que se describe el *Id del Grupo*, el *Nombre del Grupo*, los *Clientes o miembros* del grupo y las acciones para dicho grupo. 

#### Eliminar un grupo
url: `localhost:8000/api/grupos/eliminar/<id_grupo>`  
El id de grupo puede obtenerse a través de la funcionalidad *Listar grupos*, con el campo **id**.
También podemos presionar el símbolo de *"Bote de basura"* para eliminar un grupo deseado. La siguiente vista es la de confirmación de eliminación, para eliminarlo, presionar el botón *Sí, eliminar*.

#### Añadir un cliente a un grupo existente
url: `localhost:8000/api/miembros/crear/`  
También podemos seleccionar de nuestro menú de navegación la pestaña **Grupos** y posteriormente **Crear**. En la siguiente vista será necesario proporcionar un identificador para el nuevo grupo *Id* y el nombre que tendrá dicho grupo *Nombre*. Para crearlo, presionamos el botón *Crear*. Si desea cancelar la operación, presionamos el botón *Cancelar* para regresar al listado de grupos.

#### Listar miembros
url: `localhost:8000/api/miembros/listar/`  
También podemos obtener el listado de nuestros miembros a través de la pestaña del menú de navegación **Miembros**, seleccionando la opción **Listar**. Se mostrará una tabla con el *Id del miembro*, el *Id del Grupo* al que pertenece un *Cliente* en particular.

#### Editar grupos
url: `localhost:8000/api/miembros/editar/<id_miembro>`  
Para editar un grupo, es decir, reasignar un cliente a un grupo diferente, podemos partir de la tabla que muestra la funcionalidad **Listar miembros**. En la columna *Acciones*, presionamos la figura de un cuadrado con un lapiz, en la fila del grupo o del cliente que queremos editar. La siguiente vista muestra qué cliente se encuentrá en qué grupo. Si se desea reasignar el cliente seleccionado, entonces en la lista de opciones del campo *Grupo Id*, seleccionamos el id del grupo al que deseamos cambiar el cliente seleccionado.

#### Eliminar un cliente de un grupo en particular
url: `localhost:8000/api/miembros/eliminar/<id_miembro>`  
Para eliminar un cliente de un grupo en particular, de nuestra tabla de **Miembros**, en la columna *Acciones*, presionamos el símbolo del "bote de basura" para eliminar un cliente de un grupo. La siguiente vista solicitará la confirmación de la eliminación, para eliminarlo, presionamos el botón *Sí, eliminar*. Si deseamos cancelar la operación, presionamos el botón *Cancelar*, para regresar al listado de miembros.

#### Listar cuentas
url: `localhost:8000/api/cuentas/listar/`  
La url anterior nos permite saber las cuentas que están asignadas a cada grupo, así como el calendario de pagos y los pagos realizados a dicha cuenta. También podemos llegar a esa url desde la prestaña **Cuentas** del menú de navegación y seleccionando **Listar**. La vista que se mostrará es una tabla que muestra las cuentas asociadas a cada grupo. Si deseamos ver el calendario de pagos de una cuenta en particular, presionamos el enlace *Calendario de Pagos*, el cual desplegará una especie de *acordeón* con una subtabla, en la que podemos visualizar el *No. de pago*, la *Fecha de pago*, el *Monto a pagar* y el *Estatus*. De igual manera, si deseamos consultar los pagos realizados a una cuenta en particular, presionamos el enlace *Pagos realizados* para que podamos observar la subtabla con los detalles de cada pago, en este caso se presenta la *Fecha de pago* y el *Monto* pagado.


#### Crear cuenta
url: `localhost:8000/api/cuentas/crear`  
Para crear una cuenta, de la pestaña **Cuentas** del menú de navegación, seleccionamos **Crear**. En la siguiente vista deberá proporcionar el identificador de la cuenta *Id*, seleccionar el grupo al que estará asociada la cuenta *Id de Grupo*, especificar el monto y saldo de la cuenta *Monto*. El estatus automáticamente se selecciona en *DESEMBOLSADA*, puesto que es el estado inicial de la cuenta. Para crear la cuenta, presionamos el botón *Crear*. Si se desea cancelar la operación, presionamos el botón *Cancelar* y volveremos al listado de cuentas. Al crear una cuenta, automáticamente se crea su *Calendario de Pagos*.

#### Realizar un pago
url: `localhost:8000/api/transacciones/crear/`
Para realizar un pago, desde cualquier url, en la pestaña **Transacciones** del menú de navegación, seleccionamos **Crear**. En la siguiente vista se deberá proporcionar un identificador para la transacción (numérico con una longitud máxima de 6 caracteres), la cuenta a la que se va a realizar el pago *Cuenta*, la fecha en la que se realiza la transacción (presionar símbolo de calendario y seleccionar "Hoy") para llenar de manera rápida el formato de fecha y hora, y finalmente, el monto de la transacción *Monto*. Para realziar el pago presionamos el botón *Crear*. Si se desea cancelar la operación, presionamos el botón *Cancelar*.


### Validaciones adicionales
- Al crear el calendario de pagos se valida que el día de pago sea únicamente día hábil.
- Cuando una transacción se crea de manera correcta se actualiza el saldo de la cuenta. NOTA: No se especifica validación de num_pago para cada pago realizado a una cuenta, por lo que el sistema únicamente ve el pago 1. Tampoco se especifica la validación para num_pago con respecto a fecha_pago.
- Si el monto de una transacción es mayor al pago que debe ser, la transacción se rechaza.
