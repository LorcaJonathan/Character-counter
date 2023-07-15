import signal


def contador_caracteres(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isalnum():
            contador += 1
    return contador
    
while True:
    try:

        texto = input("Introduce una frase: ")

        cantidad_caracteres = contador_caracteres(texto)

        print(f"La cantidad de caracteres de la frase es: {cantidad_caracteres}")

        pregunta = input("¿Quieres introducir otra frase? (s/n)")

        if pregunta == "s" or pregunta == "S":
            continue
        elif pregunta == "n" or pregunta == "N":
            print("¡ADIOS!")
            break
        else:
            print("No es una respuesta válida, por favor responde con: (s/n)")
            print("\nSiendo s para introducir otra frase y n para salir del script.")
    except KeyboardInterrupt:
        print("\n¡ADIOS!")
        break

