"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import re

def pregunta_12():
    with open("files/input/data.csv", mode = "r") as archivo:
        data = [x.replace("\n", "") for x in archivo.readlines()]
        diccionario = {}  
        for x in [x.split("\t") for x in data]:
            key = x[0]
            columna5 = x[4]
            numeros = re.findall(r':(\d+)', columna5)
            if key in diccionario:
                diccionario[key].extend(map(int, numeros))
            else:
                diccionario[key] = list(map(int, numeros))
        
        suma_por_clave = {clave: sum(valor) for clave, valor in sorted(diccionario.items())}
        return suma_por_clave
    
        """
        Genere un diccionario que contengan como clave la columna 1 y como valor
        la suma de los valores de la columna 5 sobre todo el archivo.

        Rta/
        {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

        """