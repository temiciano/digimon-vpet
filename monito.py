import random


class Digimon:
    def __init__(self, nombre):
        if random.random() < 0.5:
            genero = "Masculino"
        else:
            genero = "Femenino"
        self.genero = genero
        self.nombre = nombre
        self.hambre = 10
        self.energia = 10
        self.etapa = "novato"
        # Aun no se usan, pero usar stats en un futuro, al dormir el mono gana x cantidad al haber gasta x cantidad de energia
        # Al dormir x cantidad el mono evoluciona
        # Mas adelante añadir diferentes evoluciones basadas en x atributos
        self.fuerza = 1
        self.agilidad = 1
        self.resistencia = 1

    def evento(self, accion):
        if accion == "alimentar":
            self.alimentar()
        elif accion == "entrenar":
            self.entrenar()

    def alimentar(self):
        print(self.nombre + " Se ha alimentado")
        self.hambre += 2
        if self.hambre >= 10:
            print(self.nombre + " No puede comer mas")
            self.hambre = 10

    def entrenar(self):
        print(self.nombre + " Ha entrenado")
        self.energia -= 2
        self.hambre -= 2
        if self.energia < 0:
            print(self.nombre() + " Esta agotado")
            self.energia = 0

    def muere(self):
        if self.hambre <= 0:
            return True
        else:
            return False

    def estadisticas(self):
        print("Hambre: " + str(self.hambre))
        print("Energia: " + str(self.energia))
        print("Genero: " + str(self.genero))
