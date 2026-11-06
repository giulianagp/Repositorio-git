from models.conexion import Conexion

class Producto:
    def __init__(self, id, codigo, nombre, precio, cantidad):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class ProductoCRUD:

    @staticmethod
    def inicializar_bd():
        # Crea la tabla y los registros iniciales si no existen
        conexion = Conexion.get_instancia()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS producto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                cantidad INTEGER NOT NULL
            )
        """)
        
        # Verificar si ya tiene datos, si está vacía insertamos los registros del tienda.sql
        cursor.execute("SELECT COUNT(*) FROM producto")
        if cursor.fetchone()[0] == 0:
            registros_iniciales = [
                ('48484', 'arroz', 45.50, 5),
                ('48485', 'frijol', 45.50, 5),
                ('48487', 'atun', 34.50, 2),
                ('48489', 'atun2', 34.50, 2)
            ]
            cursor.executemany("INSERT INTO producto (codigo, nombre, precio, cantidad) VALUES (?, ?, ?, ?)", registros_iniciales)
            conexion.commit()
        cursor.close()

    @staticmethod
    def listar():
        conexion = Conexion.get_instancia()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM producto")
        resultados = cursor.fetchall()
        cursor.close()
        return [Producto(p['id'], p['codigo'], p['nombre'], p['precio'], p['cantidad']) for p in resultados]

    @staticmethod
    def insertar(codigo, nombre, precio, cantidad):
        conexion = Conexion.get_instancia()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO producto (codigo, nombre, precio, cantidad) VALUES (?, ?, ?, ?)", (codigo, nombre, precio, cantidad))
        conexion.commit()
        cursor.close()

    @staticmethod
    def obtener_por_id(id):
        conexion = Conexion.get_instancia()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM producto WHERE id = ?", (id,))
        p = cursor.fetchone()
        cursor.close()
        if p:
            return Producto(p['id'], p['codigo'], p['nombre'], p['precio'], p['cantidad'])
        return None

    @staticmethod
    def actualizar(id, codigo, nombre, precio, cantidad):
        conexion = Conexion.get_instancia()
        cursor = conexion.cursor()
        cursor.execute("UPDATE producto SET codigo=?, nombre=?, precio=?, cantidad=? WHERE id=?", (codigo, nombre, precio, cantidad, id))
        conexion.commit()
        cursor.close()

    @staticmethod
    def eliminar(id):
        conexion = Conexion.get_instancia()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM producto WHERE id = ?", (id,))
        conexion.commit()
        cursor.close()