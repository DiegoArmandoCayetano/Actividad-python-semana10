import sqlite3

def conectar():
    conexion = sqlite3.connect("mi_base_de_datos.db")  # crea el archivo .db si no existe
    return conexion
