from base_datos import BaseDatos
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debes ingresar un número entero.")


def leer_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Error: debes ingresar un número válido.")


def mostrar_menu():

    print("\n====================================")
    print("   SISTEMA DE INVENTARIO DE VIDEOJUEGOS")
    print("====================================")
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("7. Salir")
    print("====================================")


def main():

    base_datos = BaseDatos()
    dao = ProductoDAO(base_datos)
    servicio = ProductoServicio(dao)

    while True:

        mostrar_menu()

        opcion = input("Selecciona una opción: ").strip()

        try:

            if opcion == "1":

                nombre = input("Nombre del videojuego: ")
                precio = leer_decimal("Precio: ")
                stock = leer_entero("Cantidad disponible: ")

                producto = servicio.registrar_producto(
                    nombre, precio, stock
                )

                print("Producto guardado correctamente.")
                print("ID asignado:", producto.id)

            elif opcion == "2":

                productos = servicio.listar_productos()

                if not productos:
                    print("El inventario está vacío.")

                else:
                    print("\n========== INVENTARIO ==========")

                    for producto in productos:
                        print(producto)

            elif opcion == "3":

                id_producto = leer_entero("Ingrese el ID: ")

                producto = servicio.buscar_producto(id_producto)

                if producto:
                    print("\nProducto encontrado:")
                    print(producto)

                else:
                    print("No existe un videojuego con ese ID.")

            elif opcion == "4":

                id_producto = leer_entero("Ingrese el ID a actualizar: ")

                producto = servicio.buscar_producto(id_producto)

                if producto is None:
                    print("El videojuego no existe.")

                else:
                    print("Datos actuales:")
                    print(producto)

                    nombre = input("Nuevo nombre: ")
                    precio = leer_decimal("Nuevo precio: ")
                    stock = leer_entero("Nuevo stock: ")

                    servicio.actualizar_producto(
                        id_producto, nombre, precio, stock
                    )

                    print("Producto actualizado correctamente.")

            elif opcion == "5":

                id_producto = leer_entero("Ingrese el ID a eliminar: ")

                if servicio.eliminar_producto(id_producto):
                    print("Producto eliminado correctamente.")

                else:
                    print("El videojuego no existe.")

            elif opcion == "6":

                id_producto = leer_entero("ID del videojuego: ")
                cantidad = leer_entero("Cantidad que desea vender: ")

                resultado = servicio.vender_unidades(
                    id_producto, cantidad
                )

                if resultado == "no_existe":
                    print("El videojuego no existe.")

                elif resultado == "stock_insuficiente":
                    print("Venta rechazada: stock insuficiente.")

                else:
                    print("Venta realizada correctamente.")
                    print("Stock restante:", resultado)

            elif opcion == "7":

                print("Gracias por utilizar el sistema.")
                print("Programa finalizado.")
                break

            else:

                print("Opción incorrecta. Seleccione del 1 al 7.")

        except ValueError as error:
            print("Operación rechazada:", error)

        except Exception as error:
            print("Ocurrió un error:", error)


if __name__ == "__main__":
    main()