from zooAnimales.animal import Animal

class Mamifero(Animal):
    _Mamifero = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._Mamifero.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._Mamifero)

    def isPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        Mamifero._Mamifero.append(caballo)
        return caballo

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls.leones += 1
        Mamifero._Mamifero.append(leon)
        return leon