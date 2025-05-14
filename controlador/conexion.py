from modelo.Invernadero import Invernadero
from vista.VentanaCuestionario import  VentanaCuestionario

class Conexion:
    def __init__(self):
        self.nery=NERY()

    def registrarInventario(self,datoInvernadero):
        self.nuevoInvernadero=Invernadero(*datoInvernadero)
        self.nery.guardarInvernadero(nuevoInvernadero)
        
        #self.nuevoInvernadero.setNombre(datoInvernadero[0])
        #self.objInvernadero.agregarInvernadero(nuevoInvernadero)

    def obtenerInvernaderos(self):
        return self.nery.listarInvernaderos()
