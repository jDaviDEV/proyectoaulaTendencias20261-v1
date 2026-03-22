# GRUPO 4: Gestion de ventas y facturacion


# Autenticación de Usuarios

Para hacer la autenticación se creó dos apps, una que contiene la base de datos de lo usuarios <br>
y otra que contiene la logica de autenticacion. Ambas apps tienen un endpoint para consumirlas, pero no <br>
todos los usuarios registrados tienen permisos para dicho consumo, por ejemplo, los usuarios registrados <br>
con rol contador, no pueden visualizar a los demas usuarios registrados, pero un usuario con rol administrador <br>
si puede visualzarlos.

El app de autenticacion no contiene un modelo, solo tiene una vista y un serialzer que indican al endpoint los <br>
campos requiriodos para hacer POST a la ruta /v1/login/. Para hacer solicitudes a las demás rutas se debe mandar un <br>
la solicitud HTTP con Basic Auth indicando el username y la password.

# CRUD clientes

Esta app registrada en el sistema contiene los campos: <br>

- nombre
- identificacion
- regimen_tributario
- direccion 
- email 
- telefono

Para hacer las operaciones CRUD existe el endpoint /v1/cliente y /v1/cliente/{id}, el cual recibe los 4 metodos HTTP <br>
GET para leer los datos, POST para crear un nuevo registro, DELETE para borrar un registro especificando el id, PUT o PATCH <br>
para actualizar un registro.

# CRUD Productos

Esta app registrada en el sistema contiene los campos: <br>

- nombre_producto
- codigo
- descripcion
- unidad_medida 
- precio_unitario
- porcentaje_iva
- estado

Para hacer las operaciones CRUD existe el endpoint /v1/producto y /v1/producto/{id}, el cual recibe los 4 metodos HTTP <br>
GET para leer los datos, POST para crear un nuevo registro, DELETE para borrar un registro especificando el id, PUT o PATCH <br>
para actualizar un registro.

# CRUD Cotizacion

Esta app estblece la relacion que existe entre un cliente y un producto, en el modelo queda un registro de una cotizacion, es decir,<br>
queda los clientes asociados a un producto que van a comprar, la cotizacion se calcula automaticamente dependiendo de los productos seleccionados<br>
y la cantidad a comprar. Detro del modelo se encuentran los campos: <br>

- cliente
- fecha_emision
- fecha_vencimiento
- subtotal 
- iva 
- total
- estado

Para hacer las operaciones CRUD existe el endpoint /v1/cotizacion y /v1/cotizacion/{id}, el cual recibe los 4 metodos HTTP <br>
GET para leer los datos, POST para crear un nuevo registro, DELETE para borrar un registro especificando el id, PUT o PATCH <br>
para actualizar un registro.

## Configuracion inicial:

Se procede con la ejecucion de los comandos: <br>
```
pip install django
pip install djangorestframework
pip install drf-yasg
pip install markdown
```

Con esto tenemos los paquetes necesarios para el proyecto. Dentro de la jerarquia <br>
se encuentra un requirements.txt que contiene los paquetes en la version especificada. <br>

>NOTA: el proyecto fue configurado con python 3.14.3

Para instalar estos paquetes se puede ejecutar el comando

`pip install -r requirements.txt `

Inicialmente se crearon los modelos:

-   Clientes
-   Productos
-   Cotizacion
-   ItemCotizacion
-   Usuario
-   Producto

Y para cada uno de ellos un serializer que permite la visualizacion de los datos
que se encuentran registrados en los modelos a través de un sus respectivos EndPoints
creados con django rest framework

La documentacion de los endpoints se ha realizado usando Swagger. Se puede iniciar
el servidor con el comando:

`python manage.py runserver`

Para acceder a la documentacion visite el endopint *[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)*
cuando inicialice el servidor en la máquina local