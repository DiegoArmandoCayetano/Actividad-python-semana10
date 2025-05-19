from modelo.Invernadero import Invernadero

class ListadoInvernadero:
    def __init__(self):
        self.invernaderos = []

    def agregar_invernadero(self, invernadero):
        self.invernaderos.append(invernadero)

    def obtener_todos(self):
        return self.invernaderos

    def buscar_por_id(self, id_invernadero):
        for inv in self.invernaderos:
            if inv.id_invernadero == id_invernadero:
                return inv
        return None
