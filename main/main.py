from abc import ABC, abstractmethod

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

class Caracterizacion(ABC):
    pass


class Poder(Caracterizacion):
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


class IFicha(ABC):
    pass


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



sebastian = Alien("Sebastian")

sebastian.agregar_caracterizacion(Poder("Superfuerza", "Puede levantar objetos muy pesados"))
sebastian.agregar_caracterizacion(Debilidad("Criptonita", "La criptonita lo debilita"))
sebastian.agregar_caracterizacion(Arma("Arma de protones", "Usa el arma de protones para destruir a sus enemigos"))
sebastian.agregar_caracterizacion(Arma("Super Escudo", "Este escudo lo protege de cualquier daño fisico"))
sebastian.agregar_caracterizacion(Personalidad("Carismatico", "Suele ser carismatico"))
sebastian.agregar_liga("Liga de la Justicia")
sebastian.agregar_enemigo("Lex Luthor")

ficha_sebas = sebastian.crear_ficha()

ficha_sebas.mostrar_informacion()

yorman = Humano("Yorman")

yorman.agregar_caracterizacion(Poder("Ninguno", "Los humanos no tienen poderes" ))
yorman.agregar_caracterizacion(Debilidad("Heridas por armas", "Estas heridas pueden ser perjudiciales"))
yorman.agregar_caracterizacion(Arma("Armas de fuego, armas blancas", "Estas las ayudan a defenderse"))
yorman.agregar_caracterizacion(Personalidad("Misterioso", "Suele ser misterioso"))
yorman.agregar_liga("La liga de los humanos")
yorman.agregar_enemigo("Kingpin")

ficha_yor = yorman.crear_ficha()

ficha_yor.mostrar_informacion()

Breyner = Artificial("Breyner")

Breyner.agregar_caracterizacion(Poder("Supervelocidad", "Alcanza velocidades superhumanas"))
Breyner.agregar_caracterizacion(Debilidad("Agua", "El agua podría alterar sus circuitos"))
Breyner.agregar_caracterizacion(Arma("Hackeo telequinetico", "Capaz de hackear cualquier sistema con su mente"))
Breyner.agregar_caracterizacion(Personalidad("Sin personalidad", "Es una máquina"))
Breyner.agregar_liga("La liga de los androides")
Breyner.agregar_enemigo("Deathstroke")

ficha_brey = Breyner.crear_ficha()

ficha_brey.mostrar_informacion()
