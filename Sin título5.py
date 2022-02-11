# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:23:56 2022

@author: Apawki
"""

def direction(ciudad,calle,barrio):
    print("La direccion de envio es: ")
    print("Sector ", barrio)
    print("En la calle ",calle)
    print("en la ciudad de: ", ciudad)

cl=input("ingrese la calle: ")
ba=input("Ingrese el sector: ")
ci=input("Ingrese la ciudad: ")

direction(ci, cl, ba)
