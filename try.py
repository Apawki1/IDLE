# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:11:38 2022

@author: Apawki
"""

try:
    x=int(input("Ingresa un numero: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir para cero, lo siento")
except ValueError:
    print("Debes ingresar un valor entero")
except:
    print("Oh no!, Algo malo paso")
print("Fin")

        