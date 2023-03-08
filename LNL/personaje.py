from abc import ABC, abstractmethod
from Ficha import *

class Personaje(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.liga = None
        self.enemigo = None
        self.caracterizaciones = []

    def agregar_caracterizacion(self, caracterizacion):
        self.caracterizaciones.append(caracterizacion)

    def agregar_liga(self, liga):
        self.liga = liga

    def agregar_enemigo(self, enemigo):
        self.enemigo = enemigo

    @abstractmethod
    def crear_ficha(self):
        pass


class Humano(Personaje):
    def crear_ficha(self):
        return FichaHumano(self.nombre, self.liga, self.enemigo, self.caracterizaciones)


class SuperHumano(Personaje):
    def crear_ficha(self):
        return FichaSuperHumano(self.nombre, self.liga, self.enemigo, self.caracterizaciones)


class Artificial(Personaje):
    def crear_ficha(self):
        return FichaArtificial(self.nombre, self.liga, self.enemigo, self.caracterizaciones)


class Alien(Personaje):
    def crear_ficha(self):
        return FichaAlien(self.nombre, self.liga, self.enemigo, self.caracterizaciones)
