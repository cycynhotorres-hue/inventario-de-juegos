from modelo import Producto


class ProductoServicio:

    def __init__(self, producto_dao):
        self.producto_dao = producto_dao

    def validar_datos(self, nombre, precio, stock):

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

    def registrar_producto(self, nombre, precio, stock):

        self.validar_datos(nombre, precio, stock)

        producto = Producto(
            nombre=nombre.strip(),
            precio=precio,
            stock=stock
        )

        return self.producto_dao.registrar(producto)

    def listar_productos(self):
        return self.producto_dao.listar()

    def buscar_producto(self, id_producto):

        if id_producto <= 0:
            raise ValueError("El ID debe ser positivo.")

        return self.producto_dao.buscar_por_id(id_producto)

    def actualizar_producto(self, id_producto, nombre, precio, stock):

        self.validar_datos(nombre, precio, stock)

        producto = self.buscar_producto(id_producto)

        if producto is None:
            return False

        producto.nombre = nombre.strip()
        producto.precio = precio
        producto.stock = stock

        return self.producto_dao.actualizar(producto)

    def eliminar_producto(self, id_producto):

        if id_producto <= 0:
            raise ValueError("El ID debe ser positivo.")

        return self.producto_dao.eliminar(id_producto)

    def vender_unidades(self, id_producto, cantidad):

        if id_producto <= 0:
            raise ValueError("El ID debe ser positivo.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        producto = self.producto_dao.buscar_por_id(id_producto)

        if producto is None:
            return "no_existe"

        if cantidad > producto.stock:
            return "stock_insuficiente"

        nuevo_stock = producto.stock - cantidad

        self.producto_dao.actualizar_stock(
            id_producto, nuevo_stock
        )

        return nuevo_stock