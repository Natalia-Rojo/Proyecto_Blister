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



