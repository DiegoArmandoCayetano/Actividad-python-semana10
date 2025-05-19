from modelo.Invernadero import Invernadero
from modelo.ListaInvernadero import ListadoInvernadero
from conexion import Conexion

class Controlador: 

    def __init__(self):
        self.conexion = Conexion.conectar()
        self.cursor = self.conexion.cursor()
        self.listado = ListadoInvernadero()

    def cargar_invernaderos(self):
        consulta = """SELECT id, nombre, capacidad, superficie, riego, cultivo, fecha, responsable
        FROM invernaderos"""
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()

        for id_, nombre, capacidad, superficie, riego, cultivo, fecha, responsable in resultados:
            invernadero = Invernadero(
            id_, nombre, capacidad, superficie, riego, cultivo, fecha, responsable)
            self.listado.agregar_invernadero(invernadero)

    def guardar_invernadero(self, nombre, capacidad, superficie, riego, cultivo, fecha, responsable):
        consulta = """
        INSERT INTO invernaderos (nombre, capacidad, superficie, riego, cultivo, fecha, responsable)
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (nombre, capacidad, superficie, riego, cultivo, fecha, responsable)
        self.cursor.execute(consulta, valores)
        self.conexion.commit()
