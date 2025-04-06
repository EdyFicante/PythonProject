import mysql.connector
from mysql.connector import Error
from .conexion import Conexion


class OperacionesDB:
    def __init__(self):
        self.conexion = Conexion()

    def buscar_cliente(self, ruc: str):
        """Busca un cliente por RUC en la base de datos"""
        if not self.conexion.conectar():
            return None

        try:
            cursor = self.conexion.connection.cursor(dictionary=True)
            query = """
            SELECT id, ruc_cliente, razon_social, direccion_fiscal, 
                   telefono, email, gerente_general, email_gerente, dni_gerente 
            FROM clientes_granler 
            WHERE ruc_cliente = %s 
            LIMIT 1
            """
            cursor.execute(query, (ruc,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error al buscar cliente: {e}")
            return None
        finally:
            self.conexion.cerrar()

    def actualizar_cliente(self, datos: dict):
        """Actualiza un cliente existente"""
        if not self.conexion.conectar():
            return False

        try:
            cursor = self.conexion.connection.cursor()
            query = """
            UPDATE clientes_granler SET
                razon_social = %s,
                direccion_fiscal = %s,
                telefono = %s,
                email = %s,
                gerente_general = %s,
                email_gerente = %s,
                dni_gerente = %s
            WHERE ruc_cliente = %s
            """
            cursor.execute(query, (
                datos['razon_social'],
                datos['direccion_fiscal'],
                datos['telefono'],
                datos['email'],
                datos['gerente_general'],
                datos['email_gerente'],
                datos['dni_gerente'],
                datos['ruc']  # RUC es el identificador
            ))
            self.conexion.connection.commit()
            return True
        except Error as e:
            print(f"Error al actualizar: {e}")
            return False
        finally:
            self.conexion.cerrar()

    def guardar_cliente(self, datos: dict):
        if not self.conexion.conectar():
            return False  # Retorna False si falla la conexión

        try:
            cursor = self.conexion.connection.cursor()
            query = """
            INSERT INTO clientes_granler 
            (ruc_cliente, razon_social, direccion_fiscal, telefono, email, 
             gerente_general, email_gerente, dni_gerente)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                datos['ruc'],
                datos['razon_social'],
                datos['direccion_fiscal'],
                datos['telefono'],
                datos['email'],
                datos['gerente_general'],
                datos['email_gerente'],
                datos['dni_gerente']
            ))
            self.conexion.connection.commit()
            return True  # Retorna True si se guardó correctamente

        except Error as e:
            print(f"Error al guardar: {e}")
            return False
        finally:
            self.conexion.cerrar()
