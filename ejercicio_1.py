# Escribir un programa que escriba 20 numeros aleatorios entre 100 y 1000 en un archivo llamado numeros_prueba.txt. Luego debe leer desde el archivo esos números y agregarlos a una lista, modifique o cree una nueva lista que contenga solo los numeros impares. Finalmente con numpy determinar la dimensión de la lista. Imprimir por consola la lista final y su dimensión.

import random
import numpy as np


def crear_archivo():
    with open('./numeros_prueba.txt', 'w', encoding="utf-8") as file:
        for numero in range(20):
            nr = random.randint(100, 1000)
            file.write(str(nr))
            file.write("\n")

def crear_lista():
    lista = []
    with open('./numeros_prueba.txt', 'r') as file:
        for numero in file:
            lista.append(int(numero))
    return lista

def modificar_lista(lista):
    lista_aux = []
    for elemento in lista:
        if (elemento % 2 != 0):
            lista_aux.append(elemento)
    lista = lista_aux
    return lista
    
def main():
    crear_archivo()
    lista = crear_lista()
    #print(lista)
    impares = modificar_lista(lista)
    print(impares)
    impares = np.array(impares)
    print("Dimensión: "+str(impares.ndim))

if __name__ == '__main__':
    main()