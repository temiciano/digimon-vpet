from monito import Digimon


def main():
    nombre = input("Ponle nombre a tu mascota: ").upper()
    digimon = Digimon(nombre)
    while not digimon.muere():
        digimon.estadisticas()
        eleccion = ""
        while not eleccion in ["1", "2", "3"]:
            eleccion = input("1. Alimentar \n2. Entrenar \n3. Nada \n")

        if eleccion == "1":
            digimon.evento("alimentar")

        elif eleccion == "2":
            digimon.evento("entrenar")
    print(digimon.nombre + " ha muerto")


main()
