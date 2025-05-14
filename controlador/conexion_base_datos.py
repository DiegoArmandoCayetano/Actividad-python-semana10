import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Si tienes contraseña en MySQL, ponla aquí
        database="mi_proyecto_db"
    )
    return conexion
