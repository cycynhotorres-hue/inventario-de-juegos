class Producto:
    def __init__(self, id=None, nombre="", precio=0.0, stock=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:,.2f} | "
            f"Stock: {self.stock}"
        )