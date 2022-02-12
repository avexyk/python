# -*- coding: utf-8 -*-

tupla = (1, 2.5, 'Hola')

tupla[0] # 1
tupla[1] # 2.5
tupla[2] # 'Hola'

tupla[:2] # (1, 2.5)

# Tupla vacía
tupla_vacia_1 = ()
tupla_vacia_2 = tuple()

# Tupla de un elemento
tupla_2 = (5, ) # Es una tupla
numero = (5) # Es un número

# Son inmutables
# tupla[2] = 3 # Error

# Longitud de una tupla
len(tupla)

"""Empaquetado y desempaquetado de tuplas"""
# Empaquetado
a = 30
b = "T"
c = "A"

tupla = a, b, c

# Desempaquetado
x, y, z = tupla

# Errores por distintos tamaños a desempaquetar
x, y = tupla
w, x, y, z = tupla