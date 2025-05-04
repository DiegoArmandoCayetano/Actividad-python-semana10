import mysql.connector

class conexion:
    def __init__(self):
        self.user = "root"
        self.password = ""
        self.database = "negocio"
        self.host = "localhost"

    def hacer_conexion(self):
        try:
            conex = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa...")
            return conex
        except mysql.connector.Error as err:
            print("Error de conexión:", err)
            return None
