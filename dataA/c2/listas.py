# -*- coding: utf-8 -*-

a_list = [3, 7.5, 'String', 7j + 5, [1, 2]]

# Acceso mediante indexación
a_list[0]
a_list[-1]

# Slicing
a_list[1:]
a_list[1:2]
a_list[1:3]
a_list[:2]
a_list[:]

# Algunas funciones
len(a_list) # Cantidad de elementos
a_list.append(2) # Agrega un elemento al final de la lista
a_list.extend([3, 4]) # Exntiende la lista con los elementos de otra
a_list.insert(4, 'Intercalado') # Inserta un elemento en una posición
a_list.insert(-1, 'Al final')

a_list.count(3) # Cuenta los elementos que hay que coincidad argumento
a_list.remove(3) # Elimina el primer elemento

a_list_copy = a_list.copy() # Hace una copia superficial de la lista
a_list.pop() # Saca el último elemento y lo devuelve

a_list.clear() # Limpia todos los elementos de la lista

# Similitudes de listas y strings >>>>>>>>>>
nombre = 'Francisco'
lista = list(nombre)

# Indexado
nombre[0]
lista[0]

# Slicing
nombre[:4]
lista[:4]

# len
len(nombre)
len(lista)

# in
'A' in nombre
'A' in lista

# El not in funciona en ambas
'z' not in nombre
'z' not in lista

# Los strings también se puede recorrer con un for
for letra in nombre:
  print(letra)

# Los strings son inmutables
lista[2] = 'o'
nombre[2] = 'o' # TypeError

'Hola ' + nombre
nombre + '!!'
nombre[:2] + 'o' + nombre[3:]

# Listas como pilas >>>>>>>>>>>>>>>>
# Ultimo en entrar primero en salir
stack = [1, 2, 3]

# Ingresar
stack.append(4)
stack.append(5)

# Sacar
stack.pop()
stack.pop()
stack.pop()

# Lista como colas
# Primero en entrar primero en salir
from collections import deque

# Lista como colas
queue = [1, 2, 3]

queue.append(4)
queue.append(5)

queue.pop(0)
queue.pop(0)

# Colas implementadas eficientemente en la librería estándar
queue = deque([1, 2, 3])

# Agrego los elementos
queue.append(4)
queue.append(5)

# Saco los elementos
queue.popleft()
queue.popleft()

# Listas por compresion >>>>>>>>>>>>>>>

# Lista de cuadrados
cuadrados = []
for x in range(10):
  cuadrados.append(x**2)

# Lista por compresion
cuadrados_2 = [(x ** 2) for x in range(10)]

# Cuadrados utilizando la función map
cuadrados_3 = list(map(lambda x: x**2, range(10)))

a_list = [-4, -2, 0, 2, 4]

# Lista por compresion con los números positivos de a_list
positivos = [x for x in a_list if x >= 0]

# Lista con los números positivos de a_list utilizando la función filter
positivos_2 = list(filter(lambda x: x > 0,  a_list))

# Pares de número y su cuadrado
[(x, x**2) for x in range(6)]

# Lista de pares combinados
pares = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# Equivale
pares_2 = []
for x in [1, 2, 3]:
  for y in [3, 1, 4]:
    if x != y:
      pares_2.append((x, y))