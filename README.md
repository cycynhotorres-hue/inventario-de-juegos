# Sistema de Inventario de Videojuegos

## 1. Descripción del proyecto

Este proyecto consiste en desarrollar un sistema de inventario de videojuegos utilizando Python y SQLite.

Su objetivo es facilitar la administración de videojuegos mediante operaciones que permitan registrar, consultar, actualizar y eliminar productos, además de controlar las ventas y las cantidades disponibles.

## 2. Estructura del proyecto

El proyecto está organizado en cinco archivos principales:

- modelo.py: contiene la clase Producto.
- base_datos.py: administra la conexión y creación de la base de datos SQLite.
- producto_dao.py: contiene las operaciones SQL del sistema.
- producto_servicio.py: contiene las validaciones y reglas del negocio.
- main.py: contiene el menú interactivo y permite utilizar las funciones del sistema.

## 3. Funcionalidades implementadas

1. Registrar videojuegos.
2. Mostrar el inventario.
3. Buscar videojuegos mediante su ID.
4. Actualizar información de los productos.
5. Eliminar videojuegos.
6. Vender unidades y descontarlas del inventario.
7. Salir del programa.

## 4. Validaciones

El programa cuenta con las siguientes validaciones:

- No permite nombres vacíos.
- No permite precios menores o iguales a cero.
- No permite cantidades negativas.
- No permite ventas con cantidades menores o iguales a cero.
- No permite vender más unidades de las disponibles.
- Informa cuando un videojuego no existe.
- Controla las entradas incorrectas del usuario.

## 5. Base de datos

Se utiliza SQLite para almacenar la información.

La base de datos se crea automáticamente al ejecutar el programa y conserva los registros aunque se cierre la aplicación.

## 6. Cómo ejecutar el programa

1. Instalar Python.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal.
4. Ejecutar el siguiente comando:

python main.py

No es necesario instalar librerías externas.

## 7. Pruebas de funcionamiento

Se deben realizar las siguientes pruebas:

- Registrar Resident Evil 4 con precio 180000 y stock 10.
- Mostrar el inventario.
- Buscar un videojuego existente.
- Actualizar los datos de un videojuego.
- Vender 3 unidades y comprobar que el stock quede en 7.
- Intentar vender 20 unidades y comprobar que la operación sea rechazada.
- Buscar un ID inexistente.
- Eliminar un videojuego y comprobar que desaparezca del inventario.

## 8. Evidencias

Agregar capturas de pantalla de las pruebas realizadas:

- Registro exitoso de un videojuego.
- Visualización del inventario.
- Búsqueda de un producto.
- Actualización de un producto.
- Venta exitosa.
- Venta rechazada por falta de stock.
- Eliminación de un producto.

Las capturas deben mostrar los resultados reales de la ejecución del programa.