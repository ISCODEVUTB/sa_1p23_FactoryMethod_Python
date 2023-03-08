from abc import ABC, abstractmethod

class IFicha(ABC):
    pass

class FichaArtificial(IFicha):
    def __init__(self, nombre, liga, enemigo, caracterizaciones):
        self.nombre = nombre
        self.liga = liga
        self.enemigo = enemigo
        self.caracterizaciones = caracterizaciones

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Liga: {self.liga}")
        print(f"Enemigo: {self.enemigo}")
        self.mostrar_caracterizaciones()

    def mostrar_caracterizaciones(self):
        print("Caracterizaciones:")
        for caracterizacion in self.caracterizaciones:
            print(f"- {caracterizacion.nombre}: {caracterizacion.descripcion}")


class FichaAlien(IFicha):
    def __init__(self, nombre, liga, enemigo, caracterizaciones):
        self.nombre = nombre
        self.liga = liga
        self.enemigo = enemigo
        self.caracterizaciones = caracterizaciones

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Liga: {self.liga}")
        print(f"Enemigo: {self.enemigo}")
        self.mostrar_caracterizaciones()

    def mostrar_caracterizaciones(self):
        print("Caracterizaciones:")
        for caracterizacion in self.caracterizaciones:
            print(f"- {caracterizacion.nombre}: {caracterizacion.descripcion}")



class FichaHumano(IFicha):
    def __init__(self, nombre, liga, enemigo, caracterizaciones):
        self.nombre = nombre
        self.liga = liga
        self.enemigo = enemigo
        self.caracterizaciones = caracterizaciones

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Liga: {self.liga}")
        print(f"Enemigo: {self.enemigo}")
        self.mostrar_caracterizaciones()

    def mostrar_caracterizaciones(self):
        print("Caracterizaciones:")
        for caracterizacion in self.caracterizaciones:
            print(f"- {caracterizacion.nombre}: {caracterizacion.descripcion}")
class FichaSuperHumano(IFicha):
    def __init__(self, nombre, liga, enemigo, caracterizaciones):
        self.nombre = nombre
        self.liga = liga
        self.enemigo = enemigo
        self.caracterizaciones = caracterizaciones

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Liga: {self.liga}")
        print(f"Enemigo: {self.enemigo}")
        self.mostrar_caracterizaciones()

    def mostrar_caracterizaciones(self):
        print("Caracterizaciones:")
        for caracterizacion in self.caracterizaciones:
            print(f"- {caracterizacion.nombre}: {caracterizacion.descripcion}")
