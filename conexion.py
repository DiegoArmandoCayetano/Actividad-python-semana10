import mysql.connector
class Conexion: 
    def conectar():
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",  
            database="invernaderos")
    
