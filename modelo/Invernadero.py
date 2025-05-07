class Invernadero:

    def __init__(self, nombre, superficie, tipo_cultivo, fecha_creacion, responsableInvernadero, capacidadInvernadero, sistemaRiego):
        self.nombre = nombre
        self.superficie = superficie
        self.tipo_cultivo = tipo_cultivo
        self.fecha_creacion = fecha_creacion
        self.responsableInvernadero = responsableInvernadero
        self.capacidadInvernadero = capacidadInvernadero
        self.sistemaRiego = sistemaRiego

    def getNombre(self):
        return self.nombre

    def setNombre(self, datoNombre):
        self.nombre= datoNombre

    def guardar_Invernadero(self,datoNombre):
        pass


