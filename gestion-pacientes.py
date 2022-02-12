import os
os.system('clear')
print("")
print("-----------------------------------------")
print("| ** Sistema de gestión de pacientes ** |")
print("-----------------------------------------")
print("")

# VARIABLES GLOBALES
running = True
database = list()

# FUNCIONES
def show_menu():
  print("")
  print("1 - Agregar paciente")
  print("2 - Buscar paciente")
  print("3 - Listar pacientes")
  print("4 - Salir")
  print("")
  res = input("INGRESE EL NÚMERO DE LA OPCIÓN > ")
  os.system('clear')
  return res

def response_validate(r):
  validated = False
  num_res = 0

  if response.isdigit():
    num_res = int(response)
    if num_res >= 1 and num_res <= 5:
      msg = "Número en el rango"
      validated = True
    else:
      msg = "Número fuera de rango, intente de nuevo"
  else:
    msg = "Entrada incorrecta, intente de nuevo"
  
  return validated, num_res, msg


# LOOP
while running:
  response = show_menu()
  validated, num_res, msg = response_validate(response)
  if validated:
    if num_res == 1:
      name = input("Escriba el nombre del paciente > ")
      history = input("Escriba antecedentes clínicos > ")
      paciente = {"nombre":name, "historia":history}
      database.append(paciente)
      print(database)
    elif num_res == 2:
      name = input("Escriba el nombre del paciente de su búsqueda > ")

      finded = True

      for x in range(len(database)):
        if database[x]["nombre"].lower() == name.lower():
          print("PACIENTE ENCONTRADO | H. CLINICA > ", database[x]["historia"])
        else:
          finded = False

      if(not finded):
        print("PACIENTE NO ENCONTRADO")

    elif num_res == 3:
      print("")
      print(" ----------------------------")
      print("| ** Listado de pacientes  **|")
      print(" ----------------------------")
      for x in range(len(database)):
        print("Nombre > ".ljust(10), database[x]["nombre"], "\t Historia Clinica > ".ljust(10), database[x]["historia"])
      print("FIN DE LA LISTA")

    else:
      print("")
      print("APLICACIÓN FINALIZADA")
      print("")
      running = False
  else:
    print(msg)