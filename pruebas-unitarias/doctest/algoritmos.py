"""
Cuando se hace instancia es recomensable así
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120
"""

def fibonacci(number):
  if number == 0: return 0
  elif number == 1: return 1
  else: return fibonacci(number - 1) + fibonacci(number - 2)

def palindromo(sentence):
  """ Retorna verdadero si el parámetro es un palíndromo, en caso contrario retorna falso

  sentence -- String o entero

  Implementación de test con docstring

  >>> palindromo("anita lava la tina")
  True

  >>> palindromo(12321)
  True

  >>> palindromo("Francisco")
  False
  """

  sentence = str(sentence).lower().replace(" ", "")
  # Retorna true si al inverso es lo mismo
  return sentence == sentence[::-1]

class Recursivo:
  def factorial(self, number):
    if number == 0: return 1
    else: return number * self.factorial(number - 1)

# Obtener apoyo de la librería doctest
"""python -m algoritmos.py -v
"""
if __name__ == '__main__':
  import doctest
  doctest.testmod()
  doctest.testfile("fibonacci.txt")