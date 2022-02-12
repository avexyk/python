from datetime import datetime

# Preparación
now = datetime.now()


print("Bienvenido a ... ")
print("""              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = now.year-agno-1
print()

estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
print()

sexo = input("Escribe tu género: Hombre o Mujer. ")
print()

pais = input("Nos gustaría saber de donde eres, ¿De que país nos visitas?. ")
print()

telefono = int(input("Tú teléfono te ayudará a recuperar más fácilmente tu cuenta, ¿Cuál es tú número?. "))
print()

num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("País:    ", pais)
print("Sexo:    ", sexo)
print("Teléfono:", telefono)
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")

continuar = True

while continuar:
  accion = str(input("¿Qué desea realizar?\n1. Escribir un mensaje(1)\n2. Modificar el nombre de su perfil(2)\n3. Salir(3)\n"))

  # escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))

  if accion == "1":
    mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")
  elif accion=="2":
    nombre = input("¿Cuál desea que sea su nombre ahora? ")
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", "Actualizo su nombre de perfil")
    print("--------------------------------------------------")
  elif accion=="3":
    continuar = False
  else:
    continuar = True