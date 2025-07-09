"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_01():
    with open("files/input/data.csv", mode="r") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        suma = 0
        for file in lector:
            suma += int(file[1])
    return suma
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """