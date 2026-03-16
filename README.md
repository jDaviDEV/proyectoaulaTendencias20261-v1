# GRUPO 4: Gestion de ventas y facturacion

## Configuracion inicial:

Se procede con la ejecucion de los comandos: <br>
```
pip install django <br>
pip install djangorestframework <br>
pip install markdown
```

Con esto tenemos los paquetes necesarios para el proyecto. Dentro de la jerarquia <br>
se encuentra un requirements.txt que contiene los paquetes en la version especificada. <br>

>NOTA: el proyecto fue configurado con python 3.14.3

Para instalar estos paquetes se puede ejecutar el comando

`pip install -r requirements.txt `

Inicialmente se crearon dos modelos:

-   Clientes
-   Productos

Y para cada uno de ellos un serializer que permite la visualizacion de los datos
que se encuentran registrados en los modelos a través de un sus respectivos EndPoints
creados con django rest framework