import string

print('{2} - {0} - {1}'.format(1, 2, 3))

constantes = string.hexdigits
print(constantes)

# print('{:d}'.format(2.5))
print('{:*^10}'.format('prueba'))

nro_cuenta = '32673'
saldo = 100.2543

print('El saldo de la cuenta {} es ${:.2f}'.format(nro_cuenta, saldo))
print('El saldo de la cuenta {:s} es ${:.2f}'.format(nro_cuenta, saldo))
print('El saldo de la cuenta {} es ${}'.format(nro_cuenta, saldo))
print('El saldo de la cuenta {} es ${}'.format(nro_cuenta, saldo))