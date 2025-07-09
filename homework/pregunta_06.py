
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_06():
    with open("files/input/data.csv", mode="r") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        
        diccionario = {}
        for fila in lector:
            elemento = fila[4].split(",")
            for i in elemento:
                clave, valor = i.split(":")
                valor = int(valor)
                
                if clave in diccionario:
                    diccionario[clave].append(valor)
                else: 
                    diccionario[clave] = [valor]
        lista_final = [(clave,min(valor),max(valor)) for clave, valor in diccionario.items()]
        lista_final.sort()
    return lista_final
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
