# -*- coding: utf-8 -*-

# Formas de definir un diccionario
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera':3.75}
precios = dict(manzana=3.5, banana=4.5, kiwi=6.0, pera=3.75)
precios = dict([('manzana', 3.5), ('banana', 4.5), ('kiwi', 6.0), ('pera', 3.75)])

# Acceso a los elementos por claves
precios['manzana'] # 3.5
precios['banana'] # 4.5
precios['kiwi'] # 6.0
precios['pera'] # 3.75
precios['melon'] # KeyError

# Agregar un elemento (clave-valor)
precios['melon'] = 5.75

# Actualizar un elemento (clave-valor)
precios['manzana'] = 3.0

# Borrar un elemento (clave-valor)
del precios['kiwi']

# Pertenencia
'banana' in precios
'sandia' not in precios

"""Métodos de los diccionarios"""
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera':3.75}

# Cantidad de elementos clave-valor
len(precios)

# Obtiene el valor para las clave indicada, se puede indicar un default si no existe
precios.get('manzana')
precios.get('melon')
precios.get('melon', 0.00)

# Si existe devuelve el valor, sino lo crea con el valor efault o si no se indica el default con None
precios.setdefault('banana')
precios.setdefault('sandia', 6.7)

# Actualización de un diccionario
precios.update({'banana':4.0, 'durazno':5.5})
precios.update([('durazno', 5.5)])

# Me devuelve una vista con las claves del diccionario
precios.keys()

# Me devuelve una vista con los valores del diccionario
precios.values()

# Me devuelve una vista con los items el diccionario
precios.items()

# Saca el elemento de la cave indicado, se puede poner un default si no existe
precios.pop('manzana')
precios.pop('melon', 0.00)
precios.pop('melon')

# Saca un elemento siguiendo el orden: LIFO
precios.popitem()

# Copia superficial de los diccionarios
copia_precios = precios.copy()

# Borra todos los elementos
precios.clear()

"""Iterar diccionarios"""
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera':3.75}

# Vistas de diccionarios

claves = precios.keys()
valores = precios.values()
items = precios.items()

precios['melon'] = 5.5

# Iteración de diccionarios
for fruta, precio in precios.items():
  print('Precios de', fruta, ': $', precio)

"""Claves de diccionarios"""
# Condiciones para claves de diccionarios
import datetime

a_dict = dict()

# Clave
a_dict['clave'] = 1
a_dict[1] = 1
a_dict[1.5] = 1
a_dict[(1, 2)] = 1

a_dict[datetime.date.today()] = 1

# Una lista es un contenedor no inmutable, no puede ser hasheable
a_dict[[1, 2]] = 1
# Lo mismo con los conjuntos
a_dict[{'a'}] = 1
# Lo mismo con los diccionarios
a_dict[{'a': 1}] = 1