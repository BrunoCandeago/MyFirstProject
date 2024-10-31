from abc import abstractmethod, ABC
from typing import List

class Animal(ABC):
    def __init__(self, nombre, tipo, alimentacion, habitat):
        self.alimentacion = alimentacion
        self.habitat = habitat
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        print (f"el animal {self.nombre} del tipo {self.tipo} es {self.alimentacion} y vive en {self.habitat}")

    def caminar(self):
        print (f'{self.nombre} camina')

    @abstractmethod
    def comer(self):
        pass

class AnimalAcuatico(Animal, ABC):
    def __init__(self, nombre, tipo, alimentacion, habitat):
        super().__init__(nombre, tipo, alimentacion, habitat)

    def nadar(self):
        print (f"{self.nombre} nada")

    def caminar(self):
        self.nadar()

class Leon(Animal):
    def __init__(self, nombre, tipo, alimentacion, habitat):
        super().__init__(nombre, tipo, alimentacion, habitat)

    def rugido(self):
        print (f"{self.nombre} ruge")

    def comer(self):
        print (f"{self.nombre} come carne")

class Jirafa(Animal):
    def __init__(self, nombre, tipo, alimentacion, habitat):
        super().__init__(nombre, tipo, alimentacion, habitat)

    def comer(self):
        print (f"{self.nombre} come plantas")

class Delfin(AnimalAcuatico):
    def __init__(self, nombre, tipo, alimentacion, habitat):
        super().__init__(nombre, tipo, alimentacion, habitat)

    def comer(self):
        print (f"{self.nombre} come peces")

jirafa = Jirafa('jirafa', 'nigeriana','herbivoro', 'la sabana')
leon = Leon('leon', 'del congo','carnivoro', 'bosque seco')
delfin = Delfin('delfin', 'orca', 'carnivoro', 'mar')

animales: List[Animal] = list()
animales.append(leon)
animales.append(delfin)
animales.append(jirafa)

for animal in animales:
    animal.caminar()

