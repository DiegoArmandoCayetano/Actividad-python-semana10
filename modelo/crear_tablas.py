# modelo/crear_tablas.py
from modelo.conexion import conectar

def crear_tablas():
    con = conectar()
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invernaderos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            capacidad float NOT NULL,
            superficie float not null,
            tipo varchar(30) not null,
            responsable varchar(30) not null,
            sistema_riego varchar (30) not null
        )
    ''')

    con.commit()
    con.close()
