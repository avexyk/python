import csv

someiterable = [['1', '2', '3'], ['4', '5', '6']]

with open('some.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerows(someiterable)
  
with open('example.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(['Banana', '6.50'])
  writer.writerow(['Manzana', '7.40'])

with open('names.csv', 'w', newline='') as csvfile:
  fieldnames = ['first_name', 'last_name']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  
  writer.writeheader()
  writer.writerow({'first_name': 'Pablo', 'last_name': 'Garcia'})
  writer.writerow({'first_name': 'Paula', 'last_name': 'Tina'})