import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Bakuryu1!',
    'database': 'granler_alqherramientas_db'
}


class Conexion:
    def __init__(self):
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            return True
        except Error as e:
            print(f"Error de conexión: {e}")
            return False

    def cerrar(self):
        if self.connection:
            self.connection.close()