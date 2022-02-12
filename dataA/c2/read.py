a_file = open('read.txt','r')
print(a_file.read())
print(a_file.close())

# context manager (no es necesario cerrar el archivo)
with open('read.txt', 'r') as a_file:
  a_file.read()

# Diversas formas de lectura de un archivo
with open('read.txt', 'r') as a_file:
  print(a_file.read())

with open('read.txt', 'r') as a_file:
  print(a_file.readline())

with open('read.txt', 'r') as a_file:
  print(a_file.readlines())

with open('read.txt', 'r') as a_file:
  print(list(a_file))

with open('read.txt', 'r') as a_file:
  for line in a_file:
    print(line)