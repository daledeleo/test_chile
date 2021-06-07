# Backend en Django
_Si aun no instala Python se recomienda que lo haga, ya que se asume en estos pasos que ya lo instaló._

## Comenzando 🚀

_Estas instrucciones detallas a continuación son las que se permitará levantar este aplicativo web(Backend) de manera local._


### Instalación Backend Django de python 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

1. Crear un ambiente virtual en python y activarlo (esto es opcional) explicado en [link](https://medium.com/@m.monroyc22/configurar-entorno-virtual-python-a860e820aace/)

2. Luego ubicarse en el directorio del proyecto e instalar el archivo requirements.txt
```
pip install requirements.txt
```
_Esto instalará todas las librerias necesarias para el backend_

3. Luego realizar las migraciones de los modelos a la base de datos
```
python manage.py migrate
```
_luego_
```
python manage.py makemigrations
```

_si esto falla entonces ejecutar_
```
python manage.py makemigrations core
```
_y luego_
```
python manage.py migrate
```


4. En este punto se tiene la base de datos ya desplejada en mysql en un servidor de Heroku con 5mb de espacio gratis
_luego crear un superusuario llenando todos los pasos (realize esto si la base de datos no consta con un superusuario)_

```
python manage.py createsuperuser
```
5. Y finalmente levantar el servidor de django para el backend
 ```
 python manage.py runserver
 ```
6. Creacion de usuario administrador para el inicio de sesión en el frontend
_ir a localhost:8000 en los usuario del sistema crear un usario para comenzar el login el frontend_
_Se tiene que llenar todos los campos necesarios_