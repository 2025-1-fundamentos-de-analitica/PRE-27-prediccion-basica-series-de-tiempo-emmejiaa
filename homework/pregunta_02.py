"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_02():
    with open("files/input/data.csv", mode="r") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        lista1 = [fila[0] for fila in lector]
        
        sorted(set(lista1))
        
        final = [(letra, lista1.count(letra)) for letra in sorted(set(lista1))]
    return final
        
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """