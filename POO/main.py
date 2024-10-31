from abc import abstractmethod, ABC
from typing import List
import requests

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

jirafa = Jirafa('Jirafa', 'nigeriana','herbivoro', 'la sabana')
leon = Leon('Leon', 'del congo','carnivoro', 'bosque seco')
delfin = Delfin('Delfin', 'orca', 'carnivoro', 'mar')

animales: List[Animal] = list()
animales.append(leon)
animales.append(delfin)
animales.append(jirafa)

for animal in animales:
    animal.caminar()

def dolar():
    url = "https://api.bluelytics.com.ar/v2/latest"
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()
        datos = datos["blue"]
        print (f'\nDOLAR BLUE'
               f'\n Promedio: {datos['value_avg']}'
               f'\n Precio compra: {datos['value_buy']}'
               f'\n Precio venta: {datos["value_sell"]}')
    else:
        print(f'Error {response.status_code}')

dolar()


