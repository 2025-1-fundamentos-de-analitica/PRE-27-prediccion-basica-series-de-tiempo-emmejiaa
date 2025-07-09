"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv 
import json
def pregunta_11():
    with open("files/input/data.csv", mode = "r") as archivo:
        data = [x.replace("\n", "") for x in archivo.readlines()]
        
        diccionario = {}  
        for x in [x.split("\t") for x in data]: 
            key = x[3] 
            for letra in key.replace(",",""): 
                if letra not in diccionario:
                    diccionario[letra] = int(x[1])
                else:
                    diccionario[letra] += int(x[1]) 
        diccionario = dict(sorted(diccionario.items()))
        return diccionario


        """
        Retorne un diccionario que contengan la suma de la columna 2 para cada
        letra de la columna 4, ordenadas alfabeticamente.

        Rta/
        {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


        """