# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:00:54 2022

@author: Apawki
"""

def fib(n):
    a, b = 0,1
    while a<n:
        print(a, end=" ")
        a,b=b, a+b
fib(8)
