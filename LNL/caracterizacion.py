from abc import ABC, abstractmethod

class Caracterizacion(ABC):
    pass

class Poderes(Caracterizacion):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Habilidad(Caracterizacion):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Debilidad(Caracterizacion):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Arma(Caracterizacion):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Personalidad(Caracterizacion):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion