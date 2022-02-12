# -*- coding: utf-8 -*-
import json

# serializar un objeto
json.dumps([1, 2, 3])

# deserializar un objeto
json.loads('[1, 2, 3]')

# escribir como json directamente a un archivo
with open('json_example_escribir.txt', 'w') as json_file_write:
  json.dump([1, 2, 3, 4], json_file_write)

# leer un json directamente desde un archivo
with open('json_example_leer.txt', 'r') as json_file_read:
  json_list = json.load(json_file_read)