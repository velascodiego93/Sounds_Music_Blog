# Entrega1-Velasco
Trabajo final de curso de python en CoderHouse

### DESCRIPCION DE PROYECTO
El proyecto consiste en la creacion de un blog, utilizando el framework de desarrollo web en python: Django. Se optó por realizar un blog enfocado a la creación e intercambio de contenido relacionado con la música y sonido. Todo contenido de esta índole es válido, lo que se desprende de la frase de cabecera del blog: "Si se puede escuchar, se puede debatir".

### TAREAS PREVIAS A EJECUCION DE PROYECTO
1. Descargar archivo como zip y descomprimir el contenido hacia una carpeta. Esto generará la carpeta Entrega1-Velasco-Main en la carpeta donde fue extraído el contenido
2. Abrir la carpeta Entrega1-Velasco-Main/blog_dvm dentro de la carpeta generada en el paso 2 con el editor de texto deseado.
3. Abrir una terminal y ejecutar un entorno virtual 
4. Realizar las migraciones de los modelos mediante el comando 'python manage.py migrate'
5. Correr un servidor mediante el comando 'python manage.py runserver'
6. Escribir el texto '/app_blog/index/' en el final de la URL para ir a la página de inicio de la aplicación.
7. Utilizar la aplicación libremente

### MODELOS 
Por el momento, el proyecto cuenta con tres bases de datos separadas:
- Usuarios: Estos podrían leer y publicar artículos
- Suscriptores: Estos podrían únicamente leer archivos
- Publicaciones: Las publicaciones realizadas en la página

La base de datos utilizada es db.sqlite3

### SOLICITUDES A LA BASE DE DATOS
El proyecto cuenta con formularios para ingresar datos a las tres bases de datos. Esto se hace mediante las siguientes vistas:
- Subscribe: Cuenta con un formulario para ingresar suscriptores
- Create post: Cuenta con un formulario para "publicar" en el blog. Los posts se muestran en la página de inicio (home)
- Create user: Cuenta con un formulario para ingresar usuarios
- Search post: Formulario desplegado en home para buscar posts por titulo





