from caracterizacion import *
from personaje import *
from Ficha import FichaAlien,FichaHumano, FichaArtificial, FichaSuperHumano


sebastian=Alien("Sebastian")

sebastian.agregar_caracterizacion(Poderes("Superfuerza", "Cuenta con la capacidad de levantar objetos de mayor masa"))
sebastian.agregar_caracterizacion(Debilidad("Criptonita", "La criptonita lo debilita"))
sebastian.agregar_caracterizacion(Arma("Pistola de protones", "Con esta pistola de protones puede desintegrar a niveles átomicos"))
sebastian.agregar_caracterizacion(Arma("Escudo de laseres", "Este escudo es capaz de proteger cualquier daño"))
sebastian.agregar_caracterizacion(Personalidad("Alegre", "Es muy alegre"))
sebastian.agregar_liga("Liga de la Justicia")
sebastian.agregar_enemigo("Lex Luthor")

ficha_sebas = sebastian.crear_ficha()


yorman = Humano("Yorman")

yorman.agregar_caracterizacion(Poderes("Inteligencia", "Posee una iteligencia superior al resto de su raza" ))
yorman.agregar_caracterizacion(Debilidad("Armas de cualquier tipo", "Las armas de fuego o arma blanca pueden matarlo"))
yorman.agregar_caracterizacion(Arma("Pistola", "Esta pistola es su arma más fuerte"))
yorman.agregar_caracterizacion(Personalidad("Sombrio", "Misterioso con la gente"))
yorman.agregar_liga("La liga de los humanos")
yorman.agregar_enemigo("Varon Elastico")

ficha_yor = yorman.crear_ficha()


Breyner = Artificial("Breyner")

Breyner.agregar_caracterizacion(Poderes("Hackeo telequinetico", "Puede hackear sistemas con su mente" ))
Breyner.agregar_caracterizacion(Debilidad("Agua", "El agua puede hacer corto sus circuitos"))
Breyner.agregar_caracterizacion(Arma("Espada holografica", "Esta espada es capaz de atravesar cualquier superficie"))
Breyner.agregar_caracterizacion(Personalidad("No tiene personalidad", "Es una máquina incapaz de mostrar emociones o personalidad"))
Breyner.agregar_liga("La liga de los androides")
Breyner.agregar_enemigo("Superhumanos")
ficha_brey = Breyner.crear_ficha()

print("------------------------")
print("---   La Nueva LIGA  ---")
print("------------------------")
print("--- 1) MOSTRAR       ---")
print("--- 2) AGREGAR       ---")
print("------------------------")
n=int(input("Elija una opcion "))
while(n<1 and n>2):
    
    n=int(input("Elija una opcion "))
print("------------------------")
if(n==1):
    print("Mostrar ")
    ficha_brey.mostrar_informacion()
    ficha_yor.mostrar_informacion()
    ficha_sebas.mostrar_informacion()
elif(n==2):
    
    print("----Agregar----")
    nombre = input("nombre del persona") 
    print("/////////////////////")
    print("/  1) Humano        /")
    print("/  2) Superhumano   /")
    print("/  3) Alien         /")
    print("/  4) Artificial    /")
    print("////////////////////7")
    n2=int(input("Elija la raza del personaje "))
    while(n2<1 and n2>4):
        n2=int(input("Elija la raza del personaje "))
    if(n2==1):
        print("Humano")
        raza="Humano"
    elif(n2==2):
        print("Super humano")
        raza="SuperHumano"
    elif(n2==3):
        print("alien")
        raza="Alien"
    elif(n2==4):        
        print("Artificial")
        raza="Artificial"
    poderN=input("escribe nombre del poder ")
    poderD=input("Escribe descripcion de poder")

    debilidadN=input("escribe nombre del debilidad ")
    debilidadD=input("Escribe descripcion de la debilidad")

    armaN=input("escribe nombre de la arma ")
    armaD=input("Escribe descripcion de la arma")

    personalidadN=input("escribe nombre de la personalidad ")
    personalidadD=input("Escribe descripcion de la personalidad")

    ligaN=input("Digite el nombre de la liga")
    enemigoN=input("Digite el nombre del enemigo")

    nuevo = raza(nombre)

    nuevo.agregar_caracterizacion(Poderes(poderN, poderD ))
    nuevo.agregar_caracterizacion(Debilidad(debilidadN, debilidadD))
    nuevo.agregar_caracterizacion(Arma(armaN, armaD))
    nuevo.agregar_caracterizacion(Personalidad(personalidadN, personalidadD))
    nuevo.agregar_liga(ligaN)
    nuevo.agregar_enemigo(enemigoN)
    ficha_nuevo = nuevo.crear_ficha()
    
    

    