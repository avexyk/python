import math

factorial_10 = str(math.factorial(10))
print(factorial_10)

with open('factorial.txt', 'w') as factorial:
  factorial.write(factorial_10);