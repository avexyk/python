
import random
jugar = True

while jugar == True:
  op = input('¿Tirar los dados? \n1. Sí\n2. No\n_> ')
  if op=='Sí' or op=='1':
    jugar = True
    num1 = int((random.random()*10)%6+1)
    num2 = int((random.random()*10)%6+1)
    print('Primer número: ', num1)
    print('Segundo número: ', num2)
    print('La suma de ambos números es: ', (num1+num2))
  else:
    jugar = False

print('Fin del juego')
