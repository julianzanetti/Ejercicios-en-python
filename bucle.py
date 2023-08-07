"""
# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
nombre = input("Ingrese su nombre: ")
c= 0
for i in range(10):
    c +=1
    print(nombre, c)

# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input("Ingrese su edad: "))
for i in range(edad):
    print(f"Has cumplido {i+1} años")

# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input("Ingrese un numero positivo: "))
for i in range(numero+1):
    if i % 2 !=0:
        print(i, end=",")

# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
numero = int(input("Ingrese un numero positivo: "))
for i in range(numero + 1):
    i = numero - i
    print(i, end=",")

# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
inversion = float(input("Cantidad a invertir: "))
interes_anual = float(input("Interes anual: "))
anos = int(input("Cantidad de años: "))
for i in range(anos):
    inversion = inversion + (inversion * interes_anual/100)
    print(f"Inversion en el {i+1} año: {round(inversion, 2)}")

# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****
numero = int(input("Ingrese un numero entero: "))
for i in range(numero):
    print("*" * (i+1))

# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
numero = int(input("Ingrese la altura del trangulo rectangulo: "))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contra = "contraseña"
password = input("Ingrese la palabra contraseña: ")
while password.lower() != contra:
    password = input("Ingrese la palabra contraseña: ")
print("Contraseña correcta")
"""