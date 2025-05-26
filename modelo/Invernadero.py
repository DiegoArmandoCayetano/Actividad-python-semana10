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
    def get_id_invernadero(self):
        return self.id_invernadero

    def get_nombre(self):
        return self.nombre

    def get_capacidad(self):
        return self.capacidad

    def get_superficie(self):
        return self.superficie

    def get_riego(self):
        return self.riego

    def get_cultivo(self):
        return self.cultivo

    def get_fecha(self):
        return self.fecha

    def get_responsable(self):
        return self.responsable

    # Setters
    def set_id_invernadero(self, id_invernadero):
        self.id_invernadero = id_invernadero

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def set_superficie(self, superficie):
        self.superficie = superficie

    def set_riego(self, riego):
        self.riego = riego

    def set_cultivo(self, cultivo):
        self.cultivo = cultivo

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_responsable(self, responsable):
        self.responsable = responsable
