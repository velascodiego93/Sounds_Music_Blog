# Sounds - Music blog
Trabajo final de curso de python en CoderHouse
Link a video mostrando funcionamiento de página: https://drive.google.com/file/d/12pV8F_w606QaZglMNX0q-P4pEaKQ6Shj/view
LINK ACTUALIZADO A VIDEO INCORPORANDO COMENTARIOS PARA REENTREGA: https://drive.google.com/file/d/1YpP0yf6hwrI0fY1-hfbyFvbIA7KVhtgU/view

### DESCRIPCION DE PROYECTO
El proyecto consiste en la creacion de un blog, utilizando el framework de desarrollo web en python: Django. Se optó por realizar un blog enfocado a la creación e intercambio de contenido relacionado con la música y sonido. Todo contenido de esta índole es válido, lo que se desprende de la frase de cabecera del blog: "Si se puede escuchar, se puede debatir".

### TAREAS PREVIAS A EJECUCION DE PROYECTO
1. Descargar archivo como zip y descomprimir el contenido hacia una carpeta. Esto generará la carpeta Entrega1-Velasco-Main en la carpeta donde fue extraído el contenido
2. Abrir la carpeta Entrega1-Velasco-Main/blog_dvm dentro de la carpeta generada en el paso 2 con el editor de texto deseado.
3. Abrir una terminal y ejecutar un entorno virtual 
4. Instalar paquetes de django y summernote (ver link)
5. Realizar las migraciones de los modelos mediante el comando 'python manage.py migrate'
  5.1. UPDATE: DADO QUE SE ELIMINÓ LA APP LLAMADA app_blog Y SE CREÓ LA APP accounts, ADEMÁS DE REALIZAR LAS MIGRACIONES, SE DEBE CORRER EL COMANDO python manage.py migrate --run-syncdb PARA CREAR LAS TABLAS DE LA APP accounts.
7. Correr un servidor mediante el comando 'python manage.py runserver'
9. Utilizar la aplicación libremente

### DEPENDENCIAS UTILIZADAS
- django
- summernote - La documentación oficial del editor de texto summernote se encuentra en el siguiente link:
https://github.com/summernote/django-summernote

### MODELOS 
Por el momento, el proyecto cuenta con las siguientes bases de datos separadas:
- Usuarios: Estos podrían leer y publicar artículos
- Suscriptores: Estos podrían únicamente leer archivos
- Publicaciones: Las publicaciones realizadas en la página
- Mensajes: Mensajes enviados entre usuarios
- Información extra de los usuarios: Se agrega descripción y link a una página web

La base de datos utilizada es db.sqlite3






