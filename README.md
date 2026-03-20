# GRUPO 4: Gestion de ventas y facturacion

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