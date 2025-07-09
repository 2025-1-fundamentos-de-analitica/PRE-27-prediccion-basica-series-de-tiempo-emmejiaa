"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_10():
    with open("files/input/data.csv", mode="r") as archivo:
        data = archivo.readlines()  
        
        data = [x.replace("\n", "") for x in data]  
        lista = [(x.split("\t")[0], len(x.split("\t")[3].split(',')), 
                  len(x.split("\t")[4].replace(':','').split(','))) for x in data]
        return lista
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """