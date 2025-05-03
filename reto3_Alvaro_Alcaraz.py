#voy a trastear un poco con POO y mantener el main lo mas limpio posible

class SumaInteractiva:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0

    #pedimos un numero y aseguramos que sea un numero entero (solo se usa esta funcion dentro de obtener_numeros)
    def pedir_numero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("❌ Error: por favor, ingresa un número entero.")

    #conseguimos los numeros y resultado y los guardamos
    def obtener_numeros(self):
        self.num1 = self.pedir_numero("Introduce el primer número: ")
        self.num2 = self.pedir_numero("Introduce el segundo número: ")
        self.resultado = self.num1 + self.num2

    #jugamos con los numeros
    def jugar(self):
        print(f"\nAhora te toca a ti, ¿Cuánto es {self.num1} + {self.num2}?")

        while True:
            try:
                respuesta = int(input("Tu respuesta: "))
                if respuesta == self.resultado:
                    print("✅ ¡Correcto!")
                    break
                elif respuesta < self.resultado:
                    print("🔻 Te quedaste corto, prueba de nuevo")
                else:
                    print("🔺 Te pasaste, prueba de nuevo.")
            except ValueError:
                print("❌ ERROR: ¿Cómo va a valer eso? (tip: son numeros enteros...)")

    # hacemos una funcion que nos llame a la funcion de pedir numeros y a la de jugar con ellos
    def iniciar(self):
        print("PROGRAMITA DE SUMA INTERACTIVA")
        print("==============================")
        self.obtener_numeros()
        self.jugar()


def main():
    suma = SumaInteractiva()
    suma.iniciar()


if __name__ == "__main__":
    main()
