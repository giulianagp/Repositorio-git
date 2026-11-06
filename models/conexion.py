import sqlite3

class Conexion:
    _instancia = None

    def __init__(self):
        if Conexion._instancia is not None:
            raise Exception("Esta clase es un Singleton")
        else:
            # Crea un archivo local llamado 'tienda.db' automáticamente
            self.conexion = sqlite3.connect("tienda.db", check_same_thread=False)
            self.conexion.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
            Conexion._instancia = self

    @staticmethod
    def get_instancia():
        if Conexion._instancia is None:
            Conexion()
        return Conexion._instancia.conexion