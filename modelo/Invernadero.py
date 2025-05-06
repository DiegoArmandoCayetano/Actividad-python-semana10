class Invernadero:

    def __init__(self):
       self.nombre=""
       self.apellido=""

    def getNombre(self):
        return self.nombre

    def setNombre(self, datoNombre):
        self.nombre= datoNombre

    def guardar_cliente(self,datoNombre):
        print("cliente guardado desde el modelo")
        print("se ejecuta los SQL")
        print(datoNombre)


