"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_05():
    with open("files/input/data.csv", mode="r") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        
        diccionario = {}
        
        for fila in lector:
            letra = fila[0]
            valor = int(fila[1])

            if letra in diccionario:
                diccionario[letra].append(valor)
            else:
                diccionario[letra] = [valor]
        
        diccionario1 = [(letra, max(valor), min(valor)) for letra, valor in diccionario.items()]
        diccionario1.sort()
        return diccionario1
    
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """