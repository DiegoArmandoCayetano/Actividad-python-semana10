from modelo.Invernadero import Invernadero
from controlador.conexion import Conexion
class NERY:
    pass

    def __init__(self):
        self.listaInvernadero= []

    def guardarInvernadero(self,objInvernadero):
        self.listaInvernadero.append(objInvernadero)

    def eliminarInvernadero(self,dato):
        self.listaInvernadero.remove(dato)

    def listarInvernaderos(self):
        return self.listaInvernadero
