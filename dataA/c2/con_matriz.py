# -*- coding: utf-8 -*-

"""
    CONJUNTOS EN PYTHON
"""

frutas = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana', 'kiwi'}

'pera' in frutas
'yerba' in frutas

# Conjunto vacío
set()

# Otra formas de crear conjuntos
a = set('abracadabra')
b = set('alacazam')

# Operaiones de conjuntos
a - b # letras en a pero no en b
a | b # letras en a o en b o en ambas
a & b # letras en a y en b
a ^ b # letras en a o b pero no en ambos

# Compresion de conjuntos
a = (x for x in 'abracadabra' if x not in 'abc')

# Agregar elementos al conjunto
a.add('z')

# Eliminar elementos en conjuntos
a.remove('z')

"""
    MATRICES EN PYTHON
"""

# Definición de una matriz de 3 filas x 4 columnas
matriz = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
]

# Acceso a los elementos
matriz[0][0] # 1
matriz[1][2] # 7

# Ejemplo función suma de matrices
def suma_matrices(A, B):
  """
      Suma dos matrices.
      Precondicion: A y B son del mismo tamaño y son matrices de números.
  """
  cant_filas = len(A)
  cant_cols = len(A[0])

  C = []

  for fila in range(cant_filas):
    fila_suma = []
    for col in range(cant_cols):
      fila_suma.append(A[fila][col] + B[fila][col])
      C.append(fila_suma)
  return C

suma_matrices(matriz, matriz)