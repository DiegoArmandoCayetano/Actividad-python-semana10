from modelo.Invernadero import Invernadero
from vista.VentanaCuestionario import  VentanaCuestionario
o
class Conexion:
    def __init__(self):
        self.nuevoInvernadero="+"

    def registrarInventario(self,datoInvernadero):
        self.nuevoInvernadero=Invernadero()
        self.nuevoInvernadero.setNombre(datoInvernadero[0])
        self.objInvernadero.agregarInvernadero(nuevoInvernadero)
        
