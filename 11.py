# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:29:35 2022

@author: Apawki
"""


acl=int(input("Ingrese el # de Edad " ))
if acl>=1 and acl<=13:
    print("Usted es un niño/a")
elif acl>=14 and acl<=20:
    print("Usted es un joven")
elif acl>=21 and acl<=30:
        print("Usted es una persona Adultajoven")
elif acl>=31 and acl<=50:
            print("Usted es una persona Adulta")
elif acl>=51 and acl<=100:
                print("Usted es una persona de 3ra Edad")
else: 
    print("La edad ingresada es incorrecta")
    