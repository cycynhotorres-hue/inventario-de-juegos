from modelo import Producto


class ProductoDAO:

    def __init__(self, base_datos):
        self.base_datos = base_datos

    def registrar(self, producto):
        conexion = self.base_datos.conectar()

        try:
            cursor = conexion.cursor()

            cursor.execute(
                """INSERT INTO productos
                (nombre, precio, stock)
                VALUES (?, ?, ?)""",
                (producto.nombre, producto.precio, producto.stock)
            )

            conexion.commit()
            producto.id = cursor.lastrowid

            return producto

        finally:
            conexion.close()

    def listar(self):
        conexion = self.base_datos.conectar()

        try:
            cursor = conexion.cursor()

            cursor.execute(
                "SELECT id, nombre, precio, stock FROM productos"
            )

            filas = cursor.fetchall()

            return [Producto(*fila) for fila in filas]

        finally:
            conexion.close()

    def buscar_por_id(self, id_producto):
        conexion = self.base_datos.conectar()

        try:
            cursor = conexion.cursor()

            cursor.execute(
                "SELECT id, nombre, precio, stock FROM productos WHERE id = ?",
                (id_producto,)
            )

            fila = cursor.fetchone()

            if fila:
                return Producto(*fila)

            return None

        finally:
            conexion.close()

    def actualizar(self, producto):
        conexion = self.base_datos.conectar()

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                UPDATE productos
                SET nombre = ?, precio = ?, stock = ?
                WHERE id = ?
            """, (
                producto.nombre,
                producto.precio,
                producto.stock,
                producto.id
            ))

            conexion.commit()

            return cursor.rowcount > 0

        finally:
            conexion.close()

    def eliminar(self, id_producto):
        conexion = self.base_datos.conectar()

        try:
            cursor = conexion.cursor()

            cursor.execute(
                "DELETE FROM productos WHERE id = ?",
                (id_producto,)
            )

            conexion.commit()

            return cursor.rowcount > 0

        finally:
            conexion.close()

    def actualizar_stock(self, id_producto, nuevo_stock):
        conexion = self.base_datos.conectar()

        try:
            cursor = conexion.cursor()

            cursor.execute(
                "UPDATE productos SET stock = ? WHERE id = ?",
                (nuevo_stock, id_producto)
            )

            conexion.commit()

            return cursor.rowcount > 0

        finally:
            conexion.close()