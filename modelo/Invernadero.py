from modelo.ListadoInvernadero import NERY
class Invernadero:

    def __init__(self, entry_nombre, superficie, tipo_cultivo, fecha_creacion, responsableInvernadero, capacidadInvernadero, sistemaRiego):
        self.nombre = entry_nombre
        self.superficie = superficie
        self.tipo_cultivo = tipo_cultivo
        self.fecha_creacion = fecha_creacion
        self.responsableInvernadero = responsableInvernadero
        self.capacidadInvernadero = capacidadInvernadero
        self.sistemaRiego = sistemaRiego
        self.objLista=NERY()

    def getNombre(self):
        return self.nombre

    def setNombre(self, datoNombre):
        self.nombre= datoNombre

    def guardarInvernadero(self, ListadoInvernadero):
        self.objLista.guardarInvernadero(ListadoInvernadero)


