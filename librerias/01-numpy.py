# -*- coding: utf-8 -*-
"""
Editor de Spyder

Arrays con Numpy.
"""

import numpy as np
a=np.array([1,2,3])
print('1D array:')
print(a)
print()
b=np.array([(1,2,3),(4,5,6)])
print('2D array:')
print(b)
print()

"""
Comparación de consumo entre una
lista de python y un array de numpy
"""

import sys
S=range(1000)
print('Consumo de la lista de Python')
print(sys.getsizeof(5)*len(S))
D=np.arange(1000)
print('Consumo del array de Numpy')
print(D.size*D.itemsize)
print()
print()
print()
print()
print()

"""
Rapidez
"""
import time

SIZE=1000000

L1=range(SIZE)
L2=range(SIZE)
A1=np.arange(SIZE)
A2=np.arange(SIZE)

start=time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print('Tiempo para la lista:')
print((time.time()-start)*1000)
print()
start=time.time()
result=A1+A2
print('Tiempo para el array:')
print((time.time()-start)*1000)
