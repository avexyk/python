def es_primo(numero):
  resultado = True
  i = 0
  for divisor in range(2, numero):
    i = i + 1
    print(i)
    if(numero % divisor) == 0:
      resultado = False
      break
  return resultado

es_primo(13)