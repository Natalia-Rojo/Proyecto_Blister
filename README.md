# Proyecto_Blister

Integrantes del equipo y rol a tomar:
- Diego Gutiérrez Yáñez - Mid
- José Alberto Hernández Castillo - Mid
- Héctor Emilio Cruz - Junior
- Laura Paola Torres Lozano - Junior
- Natalia Gómez Rojo - Senior

Contexto y Problema:
Actualmente, en los negocios de aplicación de pestañas no existe una herramienta organizada que permita gestionar la información de las clientas y controlar al mismo tiempo el inventario de insumos. En consecuencia, se necesita un sistema que registre a las clientas y vincule automáticamente sus solicitudes con el inventario, de manera que la lashista sepa de inmediato si puede realizar el diseño elegido según los productos disponibles, y el sistema descuente automáticamente lo utilizado en cada aplicación.

 - Problemas a resolver:

 1-. Un registro claro de los datos de las clientas (nombre, edad, tipo de aplicación, diseño solicitado).
 2-. Se desconoce en tiempo real si hay suficiente material disponible (pestañas por medidas y tipo de fibra, pegamento, pads, microbrushes, etc.) para realizar la aplicación y diseño solicitado.
 3-. La lashista debe revisar manualmente el stock, lo cual puede ocasionar errores, pérdida de tiempo y riesgo de cancelar servicios por falta de material.

 - Nuestros criterios de éxito son: 

 1-. Registro de clientas completo y ordenado
     - El sistema almacena correctamente nombre, edad, tipo de aplicación y diseño solicitado.

 2-. Gestión de inventario precisa
     - Se registra la cantidad de blisters, tiras y demás insumos disponibles.
     - El inventario se descuenta automáticamente después de cada aplicación.

 3-. Verificación automática de insumos
     - El sistema confirma si se puede realizar el servicio solicitado con los materiales actuales.
     - En caso contrario, muestra claramente qué productos faltan y en qué cantidad.

 4-. Cálculo de reposición y costos
     - El sistema cuanto hace falta para completar la aplicación.
     - El sistema indica cuánto costaría reabastecer los insumos faltantes.

 5-. Interfaz práctica para la lashista

 6-. Optimización del negocio

Reglas del Negocio:

1-. Al indicar el tipo de diseño y aplicación únicamente se pueden realizar con el Blister de acuerdo al tipo de aplicación elegido.

2-. Se deben respetar las medidas requeridas para cada diseño.

3-. Cada clienta registrada debe incluir obligatoriamente: nombre, edad, tipo de aplicación y diseño.

4-. El sistema debe asociar cada tipo de aplicación con la cantidad exacta de insumos necesarios.

5-. No se permitirá confirmar un servicio si el inventario no tiene la cantidad suficiente de insumos.

6-. En caso de inventario insuficiente, el sistema debe mostrar: insumo faltante, cantidad necesaria y costo estimado de reposición.

7-. El inventario debe descontarse automáticamente después de cada aplicación.

8.- El sistema debe permitir consultar en cualquier momento el stock disponible por insumo (blisters, tiras, pegamento, microbrush, etc.).

9-. La lashista será la usuaria principal y tendrá acceso tanto al registro de clientas como al control de inventario.


INSTRUCCIONES DE INSTALACIÓN, USO Y EQUIPO

1-. Primero se tiene que contar con la aplicación de Visual Studio Code que vas a usar solo en computadora o en lap top.
![imagen de studio code](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.20.37_506b5096.jpg)

2-. Posteriormente, se debe tener instalado Python pues es el programa con el que se va a ejecutar. 
![imagen de python](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.20.56_9891080f.jpg)

3-. Una vez con ambos programas ya instalados se creará en la sección de escritorio una carpeta vacía con el nombre de Redlash (nombre del programa).
![imagen de carpeta](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.21.09_3e6dbe64.jpg)

4-. Una vez con la carpeta creada abriremos sesión en GitHub que se puede abrir directamente desde el navegador con el que cuentes. 
![imagen de github](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.21.26_03c9a65f.jpg)

5-. Después de haber abierto sesión en GitHub, ingresaremos a este enlace para previsualizar la información del programa.
https://github.com/Natalia-Rojo/Proyecto_Blister.git

6-. Para clonar el repositorio en Visual Studio se copiará el mismo enlace previamente proporcionado (https://github.com/Natalia-Rojo/Proyecto_Blister.git) y se abrirá la aplicación de Visual Studio, para después localizar el icono de Source Control en la parte posterior izquierda de la pantalla.
![imagen de ramas](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.21.43_e8ecca64.jpg)

7-. Posteriormente se dará click en el botón de clonar repositorio.
![imagne de clone repository](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.23.41_8f5aa651.jpg)

8-. Después seleccionando la barra de búsqueda en la parte posterior se le dará click.
![imagen de buscador](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.22.02_582a6df2.jpg)

9-. Una vez ahí se pegará el enlace copiado anteriormente (https://github.com/Natalia-Rojo/Proyecto_Blister.git) y aparecerá una ventana emergente y se seleccionará la carpeta anteriormente creada seleccionando el botón de select as repository destination.
![imagen de menu carpetas](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.22.23_0ac5dfe8.jpg)

10-. Te saldrá una ventana emergente con el mensaje de si quieres abrir el repositorio clonado y le picaras en abrir. 
![imagen de aceptar clonar repositorio](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.22.37_3e43cc5b.jpg)

11-. Se puede visualizar el repositorio abierto en Visual Studio, en la parte izquierda de la pantalla deberás hacer click en el icono de unas carpetas donde aparecen una serie de documentos y el README con la información del programa. 
![imagen de files](https://github.com/Natalia-Rojo/Proyecto_Blister/blob/eea97566ef55c19de76b068839d63361c5c66fd3/data%20imagenes/Imagen%20de%20WhatsApp%202025-09-25%20a%20las%2023.23.02_4027ab05.jpg)

12-. En la carpeta docs se encuentra el reporte en PDF, manual y diagrama de flujo del código; en la carpeta src se encuentra el código fuente completo y el esqueleto del código; en la carpeta data se encuentran los archivos de prueba del código; en README se encuentra el objetivo del proyecto y roles del equipo. 



