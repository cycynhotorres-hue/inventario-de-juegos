import sqlite3


class BaseDatos:

    def __init__(self, nombre_bd="inventario_videojuegos.db"):
        self.nombre_bd = nombre_bd
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(self.nombre_bd)

    def crear_tabla(self):
        conexion = self.conectar()

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL,
                    stock INTEGER NOT NULL
                )
            """)

            conexion.commit()

        finally:
            conexion.close()