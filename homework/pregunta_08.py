"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_08():
    with open("files/input/data.csv", mode="r") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        
        dict = {}
        for row in lector:
            numbers = set(row[1])
            numbers = [int(i) for i in numbers]
            for number in numbers:
                if number in dict:
                    dict[number].append(row[0])
                else:
                    dict[number] = [row[0]]
            dict[number] = sorted(set(dict[number]))
            dict2 = sorted(dict.items())
    return dict2
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """