# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:17:34 2020

@author: avexy
"""

import numpy as np

# Matriz llena de 1
mtrzUnos=np.ones((3,4))
print(mtrzUnos)
print()

# Matriz llena de 0
mtrzCeros=np.zeros((3,4))
print(mtrzCeros)
print()

# Matriz con valores aleatorios
mtrzRandom=np.random.random((2,2))
print(mtrzRandom)
print()

# Matriz vacía
mtrzEmpty=np.empty((3,2))
print(mtrzEmpty)
print()

# Matriz con valor único
mtrzFull=np.full((2,2),8)
print(mtrzFull)
print()

# Matriz con valores patrones de separación
mtrzRange=np.arange(0,30,5)
print(mtrzRange)
mtrzRange=np.linspace(0,2,5)
print(mtrzRange)
print()

# Matriz de identidad
mtrzIden=np.eye(4,4)
print(mtrzIden)
mtrzIden=np.identity(4)
print(mtrzIden)
print()

"""
========================
"""

# Dimensiones de una matriz
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print()

# Tipo de dato de una matriz
a=np.array([(1,2,3)])
print(a.dtype)
print()

# Tamaño y forma de la matriz
a=np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)
print()

# Cambiar forma de una matriz
a=np.array([(8,9,10),(11,12,13)])
print(a)
a=a.reshape(3,2)
print(a)
print()

# Obtener el valor de una matriz
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0,2])
print()

# Obtener todos los valores de una columna
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0:,2])

# Obtener mínimo,máximo y suma
a=np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())
print()

# Raiz cuadrada y desviación estándar
a=np.array([(1,2,3),(3,4,5)])
print(np.sqrt(a))
print(np.std(a))
print()

# Suma, resta, multiplicación y división entre 2 matrices
x=np.array([(1,2,3),(3,4,5)])
y=np.array([(1,2,3),(3,4,5)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
