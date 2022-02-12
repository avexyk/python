# a_list = [(6, 2), (1, 5), (2, 3), (4, 1), (5, 2), (1, 3)]

# print(a_list.sort(key=lambda x: x[0]+x[1]))
# print(a_list.sort(lambda x: x[0]+x[1]))
# print(a_list.sort(key=x[0] + x[1]))

a_list1 = [7, 2, 3, 4, 5, 6, 1]
# print(a_list.index(1) == 6)
# print(a_list.index(4) == 3)

# print(sorted(a_list, reverse=True))

a_list = [(3, 2), (2, 4), (5, 2), (5, 3), (2, 7)]
print(a_list.sort(key=lambda x: x[1]))