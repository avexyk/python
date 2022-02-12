# -*- coding: utf-8 -*-

import json
import csv

# serializar una lista
print(json.dumps([1,2,3]))

# deserializar una lista
print(json.loads('[1,2,3]'))

# generando un archivo CSV
a_list = ['Pedro', 'Florencia', 'Matías', 'Jorge', 'María', 'Inés']

with open('generadoLista.csv', 'w', newline='', encoding='utf-8') as f:
  writer = csv.writer(f, quoting=csv.QUOTE_ALL)
  writer.writerow(a_list)

# objeto reader

reader = csv.reader(['Hola|, Mundo', 'Python'], escapechar='|')
file_content = list(reader)

print(file_content)