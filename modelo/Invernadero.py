class Invernadero:
    def __init__(self, id_invernadero, nombre, capacidad, superficie, riego, cultivo, fecha, responsable):
        self.id_invernadero = id_invernadero
        self.nombre = nombre
        self.capacidad = capacidad
        self.superficie = superficie
        self.riego = riego
        self.cultivo = cultivo
        self.fecha = fecha
        self.responsable = responsable

    def __str__(self):
        return (f"Invernadero({self.id_invernadero}, {self.nombre}, {self.capacidad}, "
                f"{self.superficie}, {self.riego}, {self.cultivo}, {self.fecha}, {self.responsable})")
