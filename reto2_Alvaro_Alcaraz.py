"""
Reto 2
Enunciado:
¿Qué es un Palíndromo?
Una palabra o frase que se lee igual de izquierda a derecha que de derecha a
izquierda.
Por Ejemplo.
• Reconocer
• No traces en ese cartón
• Sometamos o matemos
• Isaac no ronca así
El programa consistirá en pedir una frase o palabra al usuario y decirle si es un
Palíndromo o no lo es.

"""

#Una version mejorada, porque ya que descubri la biblioteca unicodedata decidi trastear mas
import unicodedata
import re


def limpiar_texto(texto):
    #fuera signos de puntuacion y caracteres especiales al texto
    texto = re.sub(r'[^\w\s]', '', texto)
    #descubrir esto de aqui arriba fue algo expectacular
    #print(texto)
    #fuera acentos y cosas raras
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    #print(texto)
    #fuera los espacios y lo hacemos en minusculas
    return texto.lower().replace(" ", "")


def es_palindromo(texto):
    texto_limpio = limpiar_texto(texto)
    #print(texto_limpio)
    return texto_limpio == texto_limpio[::-1]


def main():
    print("SUPER VERIFICADOR DE PALINDROMOS DE ALTO NIVEL")
    print("=============================================")
    print("Puedes poner las palabras con todo esto que quieras:")
    print("- Mayúsculas/minúsculas")
    print("- Acentos y caracteres especiales")
    print("- Espacios entre palabras")
    print("- Signos de puntuación")
    print("\nIngresa una palabra o frase. Escribe 'salir' para terminar.")

    while True:
        entrada = input("> ").strip()

        if entrada.lower() == "salir":
            print("¡Adios!")
            break

        if not entrada:
            print("Error: No has ingresado nada")
            continue

        if es_palindromo(entrada):
            print(f"\n✅ '{entrada}' SÍ es un palíndromo!")
        else:
            print(f"\n❌ '{entrada}' NO es un palíndromo")
        #descubri los emoticonos y hace que sea t0do mas bonito


if __name__ == "__main__":
    main()
