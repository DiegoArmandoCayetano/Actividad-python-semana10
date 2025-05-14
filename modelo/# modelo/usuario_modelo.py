from conexion import conectar

def agregar_usuario(nombre, edad):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    con.commit()
    con.close()

def obtener_usuarios():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    con.close()
    return usuarios
