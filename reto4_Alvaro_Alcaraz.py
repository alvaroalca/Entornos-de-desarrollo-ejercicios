"""version mejorada que ademas me pregunta que quiero hacer y
    tambien añade si el personaje a revivido o ya esta muerto y no puede perder mas vida
"""
class Soldado:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.fuerza = 100
        #estado me sirve para ver si el pj esta muerto o no
        self.estado = "vivo"

    def perdida(self, valor):
        #le quitamos vida al pj
        if self.estado == "muerto":
            print()
            print("Tu personaje ya está muerto...")
            #return para que no ejecute nada mas, ya esta muerto
            return
        #restamos el valor asignado y vemos si muere el pj
        self.fuerza -= valor
        if self.fuerza <= 0:
            #no podemos tener vida negativa aunque nos hagan -9999
            self.fuerza = 0
            self.estado = "muerto"
            print()
            print("Tu personaje ha muerto...☠️")
        else:
            print()
            print(f"Tu personaje ha perdido {valor} de fuerza. Ahora tienes {self.fuerza} puntos de fuerza.")

    def ganancia(self, valor):
        #añadimos vida al pj
        if self.estado == "muerto":
            self.fuerza += valor
            if self.fuerza > 100:
                #maxeamos la fuerza a 100
                self.fuerza = 100
            self.estado = "vivo"  #revivimos
            print()
            print(f"Tu personaje ha ganado {valor} de fuerza y ha revivido🤩. Ahora tienes {self.fuerza} puntos de fuerza.")
        else:
            self.fuerza += valor
            if self.fuerza > 100:
                #lo mismo de antes, maxeamos la fuerza a 100
                self.fuerza = 100
            print()
            print(f"Tu personaje ha ganado {valor} fuerza. Ahora tienes {self.fuerza} puntos de fuerza.")


#creamos al pj
soldado = Soldado(peso=99.8, altura=137) #si, es un enano


#aqui pasa toda la magia
def menu():
    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Restar fuerza")
        print("2. Sumar fuerza")
        print("Escribe 'salir' para terminar.")
        #nos quitamos de problemas y le hacemos el strip y minusculas directamente aqui
        opcion = input("Selecciona una opción: ").strip().lower()

        if opcion == "salir":
            print("¡Adios!")
            break
        elif opcion == "1":  #elegimos restar fuerza
            try:
                valor = int(input("¿Cuánto quieres restar de fuerza? "))
                if valor < 0:
                    print()
                    print("Eso es imposible, esto es a prueba de bugs.")
                else:
                    soldado.perdida(valor)
            except ValueError:
                print()
                print("Por favor, ingresa un número válido para la fuerza.")
        elif opcion == "2":  #elegimos sumar fuerza
            try:
                valor = int(input("¿Cuánto quieres sumar de fuerza? "))
                if valor < 0:
                    print()
                    print("Eso es imposible, esto es a prueba de bugs.")
                else:
                    soldado.ganancia(valor)
            except ValueError:
                print()
                print("Por favor, ingresa un número válido para la fuerza.")
        else:
            print()
            print("Opción no válida. Por favor, selecciona una opción correcta.")


if __name__ == '__main__':
    menu()

