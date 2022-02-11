# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:07:22 2022

@author: Apawki
"""

def readint(prompt, min, max):
    try:
        num = int(input(prompt))
        assert num >= min and num <= max
        return num
    except ValueError:
        print("Error: entrada incorrecta")
        return readint(prompt, min, max)
    except AssertionError:
        print("Error: el valor no está dentro del rango permitido")
        return readint(prompt, min, max)
  


v = readint("Ingrese un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
