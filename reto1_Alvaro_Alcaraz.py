"""Realiza el diagrama de flujo para resolver el siguiente problema:
Leer un par de números (x,y) y hallar el cuadrante del plano en el que se encuentra, devolviendo un valor entre 1 y 4 tal que:
(+x,+y) es cuadrante 1, (+x,-y) es cuadrante 2, (-x,-y) es cuadrante 3 y (-x,+y) es cuadrante 4"""
while True:
    try:
        entrada_x = input("Ingresa el valor de x (o escribe 'salir' para terminar): ")
        if entrada_x.lower() == "salir":
            break
        entrada_y = input("Ingresa el valor de y (o escribe 'salir' para terminar): ")
        if entrada_y.lower() == "salir":
            break

        x = float(entrada_x)
        y = float(entrada_y)

        # Determinar la ubicación
        if x > 0 and y > 0:
            print("Cuadrante 1")
        elif x > 0 and y < 0:
            print("Cuadrante 2")
        elif x < 0 and y < 0:
            print("Cuadrante 3")
        elif x < 0 and y > 0:
            print("Cuadrante 4")
        elif x == 0 and y == 0:
            print("El punto está en el origen")
        elif x == 0 or y == 0:
            print("El punto está sobre un eje (no pertenece a ningún cuadrante)")

    except ValueError:
        print("Error: Ingresa solo números válidos.")
