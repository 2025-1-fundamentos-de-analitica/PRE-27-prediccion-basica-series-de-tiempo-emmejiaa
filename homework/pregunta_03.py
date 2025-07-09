"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_03():
    with open("files/input/data.csv", mode="r") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        
        conteo = {}
        
        for fila in lector:
            if fila[0] not in conteo:
                conteo[fila[0]] = 0
            conteo[fila[0]] += int(fila[1])
        
        resultado = [(letra, suma) for letra, suma in conteo.items()]
        resultado.sort()
        return resultado
        
    """
    Otra forma de hacerlo con diccionarios 
        
        conteo = {}
        
        for fila in lector:
            letra = fila[0]
            valor = int(fila[1])

            if letra in conteo:
                conteo[letra] += valor
            else:
                conteo[letra] = valor
                
        resultado = sorted(conteo.items())
        print(resultado)   
    
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """