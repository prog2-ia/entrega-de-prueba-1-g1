def leer_notas():
    """
    Pide al usuario notas separadas por espacios y devuelve una lista de floats.
    Por ejemplo: 5 7.5 9 10
    """
    texto = input("Introduce las notas separadas por espacios: ")
    partes = texto.split()
    notas = []
    for p in partes:
        notas.append(float(p))
    return notas
    
def calcular_media(notas):
    """
    Devuelve la media de una lista de notas (floats).
    """
    if len(notas) == 0:
        return 0.0

    suma = 0.0
    for n in notas:
        suma = suma + n

    return suma / len(notas)


def mostrar_resumen(notas):
    """
    Muestra por pantalla:
    - Número de notas
    - Nota máxima
    - Nota mínima
    - Nota media
    """
    if len(notas) == 0:
        print("No se han introducido notas.")
        return

    maximo = notas[0]
    minimo = notas[0]

    i = 0
    while i < len(notas):
        if notas[i] > maximo:
            maximo = notas[i]
        if notas[i] < minimo:
            minimo = notas[i]
        i = i + 1

    media = calcular_media(notas)

    print("Número de notas:", len(notas))
    print("Nota máxima:", maximo)
    print("Nota mínima:", minimo)
    print("Nota media:", round(media, 2))


if __name__ == "__main__":
    notas = leer_notas()
    mostrar_resumen(notas)

# funciona