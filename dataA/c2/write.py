with open('write.txt', 'w') as a_file:
  a_file.write('Escritura 1')

with open('write.txt', 'w') as a_file:
  a_file.writelines('Escritura 1.\n','Escritura 2.\n','Escritura 3.\n')

with open('write.txt', 'a') as a_file:
  a_file.write('Escritura 4 al final')