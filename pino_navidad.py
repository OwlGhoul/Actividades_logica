# -*- coding: utf-8 -*-
"""Pino_navidad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1khPtSQEJt9NIkBGu723l6AG231RjZkdu
"""

def imprimir_pino(filas):
    # Imprimir la parte superior del pino
    for i in range(filas):
        for j in range(filas - i):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    # Imprimir el tronco del pino
    for i in range(2):
        for j in range(filas - 1):
            print(" ", end="")
        print("")

# Solicitar al usuario la cantidad de filas para el pino
filas = int(input("Ingrese el número de filas para el pino: "))

# Llamar a la función para imprimir el pino
imprimir_pino(filas)