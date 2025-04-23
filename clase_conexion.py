import mysql.connector

class conexion:
    def __init__(self):
        self.user="root"
        self.password=""
        self.database="negocio"
        self.host="localhost"

    def hacer_conexion(self):
        conex= mysql.connector.connect(self.host,self.database,self.user,self.password)
        try:
            if conex.connect():
                print("Conexión con Exito.....")
        except:
            print("Error de Conexión.....")
        return conex
        