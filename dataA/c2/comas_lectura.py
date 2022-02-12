import csv

with open('some.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)
    
with open('passwd', newline='') as f:
  reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
  for row in reader:
    print(row)

with open('example.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in reader:
    print(', '.join(row))

csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('passwd', newline='') as f:
  reader = csv.reader(f, 'unixpwd')

import csv

# Clase DictReader
with open('names.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row['first_name'], row['last_name'])