# import random

# matrizjuego = [[0,1,2],[4,5,6]]

# print(matrizjuego)

# print(matrizjuego.index())

# t = [(index, row.index('|_|')) for index, row in enumerate(matrizjuego) if '|_|' in row]

# s = [(index) for index, row in enumerate(matrizjuego) if '|_|' in row]

# if not s:
#   print('Vacia')
# else:
#   print('Tiene algo')

  
# cuadro = input("Es tu turno\n_>")

# bando = 'O'

# if cuadro == '1' and not matrizjuego[0][0] == '|X|' and not matrizjuego[0][0] == '|O|':
#   matrizjuego[0][0] = '|'+bando+'|'
# else:
#   print('Cuadro ocupado, intente de nuevo')

# for i in range(len(matrizjuego)):
#     for j in range(len(matrizjuego[i])):
#         print(matrizjuego[i][j], end=' ')
#     print()

# def rival():
#   movimiento = random.randrange(1, 10)
#   return movimiento

# print("Es turno de la computadora...")
# print(rival())

def ganadorPartida(M):
  g1x = M[0][0] == '|X|'
  g2x = M[0][1] == '|X|'
  g3x = M[0][2] == '|X|'
  g4x = M[1][0] == '|X|'
  g5x = M[1][1] == '|X|'
  g6x = M[1][2] == '|X|'
  g7x = M[2][0] == '|X|'
  g8x = M[2][1] == '|X|'
  g9x = M[2][2] == '|X|'

  g1o = M[0][0] == '|O|'
  g2o = M[0][1] == '|O|'
  g3o = M[0][2] == '|O|'
  g4o = M[1][0] == '|O|'
  g5o = M[1][1] == '|O|'
  g6o = M[1][2] == '|O|'
  g7o = M[2][0] == '|O|'
  g8o = M[2][1] == '|O|'
  g9o = M[2][2] == '|O|'

  result = False
  
  if g1x and g2x and g3x:
    result = True
  elif g4x and g5x and g6x:
    result = True
  elif g7x and g8x and g9x:
    result = True
  elif g1x and g4x and g7x:
    result = True
  elif g2x and g5x and g8x:
    result = True
  elif g3x and g6x and g9x:
    result = True
  elif g1x and g5x and g9x:
    result = True
  elif g3x and g5x and g7x:
    result = True
  elif g1o and g2o and g3o:
    result = True
  elif g4o and g5o and g6o:
    result = True
  elif g7o and g8o and g9o:
    result = True
  elif g1o and g4o and g7o:
    result = True
  elif g2o and g5o and g8o:
    result = True
  elif g3o and g6o and g9o:
    result = True
  elif g1o and g5o and g9o:
    result = True
  elif g3o and g5o and g7o:
    result = True
  else:
    result = False
  
  return result

matrizjuego = [['|X|','|_|','|X|'], ['|X|','|O|','|O|'], ['|O|','|O|','|_|']]

print(ganadorPartida(matrizjuego))

  # def verificaEmpate():
  #   print("Función verificaEmpate")

  # def computadora():
  #   movimiento = random.randrange(1, 10)
  #   return movimiento