import random


class Digimon:
    def __init__(self, nombre):
        if random.random() < 0.5:
            genero = "MALE"
        else:
            genero = "FEMALE"
        self.genero = genero
        self.nombre = nombre
        self.hambre = 10
        self.energia = 5
        self.etapa = "novato"
        self.days = 0
        # Aun no se usan, pero usar stats en un futuro, al dormir el mono gana x cantidad
        # Al dormir x cantidad el mono evoluciona
        # Mas adelante añadir diferentes evoluciones basadas en x atributos
        self.fuerza = 1
        self.agilidad = 1
        self.resistencia = 1

    def evento(self, accion):
        if accion == "FEED":
            self.alimentar()
        elif accion == "TRAIN":
            self.entrenar()
        elif accion == "SLEEP":
            self.dormir()

    def alimentar(self):
        print(self.nombre + " Se ha alimentado")
        self.hambre += 2
        if self.hambre >= 10:
            print(self.nombre + " No puede comer mas")
            self.hambre = 10

    def entrenar(self):
        if self.energia > 0:
            print(self.nombre + " Ha entrenado")
            self.energia -= 1
            self.hambre -= 2
        else:
            print(self.nombre + " Esta agotado y no puedo entrenar mas")
            self.energia = 0

    def muere(self):
        if self.hambre <= 0:
            return True
        else:
            return False

    def power_up(self):
        stats = {'fuerza': self.fuerza, 'agilidad': self.agilidad,
                 'resistencia': self.resistencia}
        stat_elegido = random.choice(list(stats.keys()))

        if stat_elegido == 'fuerza':
            self.fuerza += 1
        elif stat_elegido == 'agilidad':
            self.agilidad += 1
        elif stat_elegido == 'resistencia':
            self.resistencia += 1

    def dormir(self):
        # Sumar puntos. While para que sume un punto a energia, y cada punto recuperado se suma una caracteristica aleatoria
        while self.energia < 5:
            self.power_up()
            self.energia += 1
            print(self.nombre + " Ha despertado al dia siguiente")
            self.days += 1

    def estadisticas(self):
        print("Hambre: " + str(self.hambre))
        print("Energia: " + str(self.energia))
        print("Genero: " + str(self.genero))
        print("Dias transcurridos: " + str(self.days))
        print("STATS: " + "Fuerza: " + str(self.fuerza) + " " + "Agilidad: " +
              str(self.agilidad) + " " + "Resistencia: " + str(self.resistencia))
