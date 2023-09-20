from zooAnimales.animal import Animal


class Anfibio(Animal):
    _Anfibio = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._Anfibio.append(self)
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._Anfibio)

    def isVenenoso(self):
        return self._venenoso

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        Anfibio._Anfibio.append(rana)
        return rana

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        Anfibio._Anfibio.append(salamandra)
        return salamandra

