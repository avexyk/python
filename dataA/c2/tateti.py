# -*- coding: utf-8 -*-
import random

print("\n***** BIENVENIDO A TA-TE-TI ******\n")
jugar = input("¿Desea crear una nueva partida?\n1. Si\n2. No\n3. Cualquier otra tecla para salir\n_> ")

turnoX = True

if jugar=='Si' or jugar=='1':
  print("\n|_| |_| |_|\n|_| |_| |_|\n|_| |_| |_|")

  bando = ''
  b = True

  while b:
    bando = input("\n¿Con qué desea jugar?\n1. X\n2. O\n_> ")
    # Elección del bando
    if bando=='1' or bando=='X' or bando=='2' or bando=='O':
      if bando=='1' or bando=='X':
        bando='X'
        turnoX = True
      elif bando=='2' or bando=='O':
        bando='O'
        turnoX = False
      b = False
    else:
      print("\n¡¡Opción no válida!!")
      b = True

  print("\nUsted eligió jugar con: ", bando, "\n=====[Leer las siguientes instrucciones:]")
  print("\n|1| |2| |3|\n|4| |5| |6|\n|7| |8| |9|\n")
  print("[ Se usará la notación presentada en la cuadrícula anterior.\n  Cada número representa un cuadro. Para elegir agregar la\n  'X' u 'O' en un cuadro tendrá que elegir un número...    ]")
  print("\nLas X empiezan\n")

  bando='X'
  turnoX=True

  matrizjuego = [['|_|','|_|','|_|'], ['|_|','|_|','|_|'], ['|_|','|_|','|_|']]
  partida = True # Termina la partida con un ganador o empate
  cuadricula = True
  empate = False

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

  while partida:
    # Inicia la partida
    # Revision de la cuadricula

    victoria = ganadorPartida(matrizjuego)
    s = [(index) for index, row in enumerate(matrizjuego) if '|_|' in row]

    if not s and victoria==False:
    # Cuadricula llena
      partida = False
      # empate = True

      for i in range(len(matrizjuego)):
          for j in range(len(matrizjuego[i])):
              print(matrizjuego[i][j], end=' ')
          print()
      
      print('\n+++ LA PARTIDA A TERMINADO EN EMPATE +++')
      break
    elif not s and victoria:
      # Cuadricula todavia tiene un espacio
      print('\n+++ LA PARTIDA A TERMINADO +++')

      if bando=='X':
        bando='O'
      elif bando=='O':
        bando='X'

      print('\n+++ GANAROR: ', bando)
      partida = False

      for i in range(len(matrizjuego)):
          for j in range(len(matrizjuego[i])):
              print(matrizjuego[i][j], end=' ')
          print()

      break
    elif s and victoria:
      print('\n+++ LA PARTIDA A TERMINADO +++')

      if bando=='X':
        bando='O'
      elif bando=='O':
        bando='X'

      print('\n+++ GANAROR: ', bando)
      partida = False

      for i in range(len(matrizjuego)):
          for j in range(len(matrizjuego[i])):
              print(matrizjuego[i][j], end=' ')
          print()

      break
      
    if bando=='X':
      # Turno de X
      while turnoX:
        for i in range(len(matrizjuego)):
            for j in range(len(matrizjuego[i])):
                print(matrizjuego[i][j], end=' ')
            print()
        cuadro = input("Es el turno de X:\n_> ")

        if cuadro == '1' and not matrizjuego[0][0] == '|X|' and not matrizjuego[0][0] == '|O|':
          matrizjuego[0][0] = '|'+bando+'|'
          bando='O'
          turnoX = False
        elif cuadro == '2' and not matrizjuego[0][1] == '|X|' and not matrizjuego[0][1] == '|O|':
          matrizjuego[0][1] = '|'+bando+'|'
          bando='O'
          turnoX = False
        elif cuadro == '3' and not matrizjuego[0][2] == '|X|' and not matrizjuego[0][2] == '|O|':
          matrizjuego[0][2] = '|'+bando+'|'
          bando='O'
          turnoX = False
        elif cuadro == '4' and not matrizjuego[1][0] == '|X|' and not matrizjuego[1][0] == '|O|':
          matrizjuego[1][0] = '|'+bando+'|'
          bando='O'
          turnoX = False
        elif cuadro == '5' and not matrizjuego[1][1] == '|X|' and not matrizjuego[1][1] == '|O|':
          matrizjuego[1][1] = '|'+bando+'|'
          bando='O'
          turnoX = False
        elif cuadro == '6' and not matrizjuego[1][2] == '|X|' and not matrizjuego[1][2] == '|O|':
          matrizjuego[1][2] = '|'+bando+'|'
          bando='O'
          turnoX = False
        elif cuadro == '7' and not matrizjuego[2][0] == '|X|' and not matrizjuego[2][0] == '|O|':
          matrizjuego[2][0] = '|'+bando+'|'
          bando='O'
          turnoX = False
        elif cuadro == '8' and not matrizjuego[2][1] == '|X|' and not matrizjuego[2][1] == '|O|':
          matrizjuego[2][1] = '|'+bando+'|'
          bando='O'
          turnoX = False
        elif cuadro == '9' and not matrizjuego[2][2] == '|X|' and not matrizjuego[2][2] == '|O|':
          matrizjuego[2][2] = '|'+bando+'|'
          bando='O'
          turnoX = False
        else:
          print('Cuadro ocupado o fuera de rango, intente de nuevo')
    else:
      # Turno de O
      while turnoX == False:
        for i in range(len(matrizjuego)):
            for j in range(len(matrizjuego[i])):
                print(matrizjuego[i][j], end=' ')
            print()
        cuadro = input("Es el turno de O:\n_> ")

        if cuadro == '1' and not matrizjuego[0][0] == '|X|' and not matrizjuego[0][0] == '|O|':
          matrizjuego[0][0] = '|'+bando+'|'
          bando='X'
          turnoX = True
        elif cuadro == '2' and not matrizjuego[0][1] == '|X|' and not matrizjuego[0][1] == '|O|':
          matrizjuego[0][1] = '|'+bando+'|'
          bando='X'
          turnoX = True
        elif cuadro == '3' and not matrizjuego[0][2] == '|X|' and not matrizjuego[0][2] == '|O|':
          matrizjuego[0][2] = '|'+bando+'|'
          bando='X'
          turnoX = True
        elif cuadro == '4' and not matrizjuego[1][0] == '|X|' and not matrizjuego[1][0] == '|O|':
          matrizjuego[1][0] = '|'+bando+'|'
          bando='X'
          turnoX = True
        elif cuadro == '5' and not matrizjuego[1][1] == '|X|' and not matrizjuego[1][1] == '|O|':
          matrizjuego[1][1] = '|'+bando+'|'
          bando='X'
          turnoX = True
        elif cuadro == '6' and not matrizjuego[1][2] == '|X|' and not matrizjuego[1][2] == '|O|':
          matrizjuego[1][2] = '|'+bando+'|'
          bando='X'
          turnoX = True
        elif cuadro == '7' and not matrizjuego[2][0] == '|X|' and not matrizjuego[2][0] == '|O|':
          matrizjuego[2][0] = '|'+bando+'|'
          bando='X'
          turnoX = True
        elif cuadro == '8' and not matrizjuego[2][1] == '|X|' and not matrizjuego[2][1] == '|O|':
          matrizjuego[2][1] = '|'+bando+'|'
          bando='X'
          turnoX = True
        elif cuadro == '9' and not matrizjuego[2][2] == '|X|' and not matrizjuego[2][2] == '|O|':
          matrizjuego[2][2] = '|'+bando+'|'
          bando='X'
          turnoX = True
        else:
          print('Cuadro ocupado o fuera de rango, intente de nuevo')
  
else:
  print("\nAdiós...")