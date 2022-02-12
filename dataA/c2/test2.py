
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a_list)

a_list_sub = a_list[1:8]
print(a_list_sub)

a_list_sub.insert(9, 9)
print(a_list_sub)

a_list_sub.insert(0, 5)
print(a_list_sub)

a_list_sub.remove(5)
print(a_list_sub)

a_list_sub.remove(9)
print(a_list_sub)

print('\n> Lista de compresión')
pares = [x for x in range(1, 101) if x % 2 == 0]
print(pares)

# Final test
lista_test = [x*y for x in [1,2,3] for y in [3,1,4] if x != y]
print(lista_test)

lista_dada = [1, 3, 5, 7, 9]
print('Buscar ', lista_dada)

primera = [x for x in range(10) if x % 2 == 1]
segunda = [x for x in range(10) if x % 2 != 1]
tercera = [x * 2 + 1 for x in range(5)]
cuarto = [x for x in range(10) if x % 2 == 0]
quinto = [x for x in range(10) if x % 2 != 0]

print('\n', primera, '\n', segunda, '\n', tercera, '\n', cuarto, '\n', quinto)