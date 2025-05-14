# modelo/crear_tablas.py
from modelo.conexion import conectar

def crear_tablas():
    con = conectar()
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            edad INT NOT NULL
        )
    ''')

    con.commit()
    con.close()
