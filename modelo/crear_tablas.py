from modelo.conexion import conectar  # Asegúrate de que conexion.py esté también en modelo/

def crear_tablas():
    con = conectar()
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    ''')

    con.commit()
    con.close()
