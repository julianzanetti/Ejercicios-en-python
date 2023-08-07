#Ejercicio 1
print("Hola mundo")

#Ejercicio 2
saludo = "Hola mundo"
print(saludo)

#Ejercicio 3
nombre = input("Escribe tu nombre: ")
print(f"Hola {nombre}")

#Ejercicio 4
operacion = ((3+2)/(2*5))**2
print (f"La siguiente operacion ((3+2)/(2*5))**2 da como resultado: {operacion}")

#Ejercicio 5
horas = float(input("Ingrese la cantidad de horas trabajadas: "))
costo = float(input("Ingrese la paga correspondiente por hora: "))
paga = float(costo * horas)
print(f"La paga es la siguiente: {paga}$")

#Ejercicio 6
n = int(input("Ingrese un entero positivo: "))
suma = n*(n+1)/2
print(f"La suma de los {n} primeros enteros positivos es {suma}")

#Ejercicio 7
peso = float(input("Ingrese su peso (kg): "))
estatura = float(input("Ingrese su estatura en metros: "))
imc = round(peso/estatura**2, 2)
print(f"El indice de masa corporal es {imc}")

#Ejercicio 8
n = int(input("Ingrese un numero entero: "))
m = int(input("Ingrese otro numero entero: "))
c = n // m
r = n % m
print(f"El cociente de {n} y {m} es {c} y el resto es {r}")

#Ejercicio 9
inversion = float(input("Ingrese un monto a invertir: "))
interes = int(input("Ingrese el interes anual %: "))
años = int(input("Ingrese la cantidad de años: "))
capital = inversion * (interes / 100 + 1) ** años
print(f"El capital obtenido es {capital}")

#Ejercicio 10
payaso = 112
muñeca = 75
cant_pay = int(input("Ingrese la cantidad de payasos vendidos en el ultimo pedido: "))
cant_muñe = int(input("Ingrese la cantidad de muñecas vendidas en el ultimo pedido: "))
peso_total = (payaso * cant_pay) + (muñeca * cant_muñe)
print(f"El peso total del pedido es {peso_total}kg")

#Ejercicio 11
interes_anual = 0.04
caja_ahorro = int(input("Dinero depositado: "))
c = 0
for i in range(3):
    aux = caja_ahorro * interes_anual
    caja_ahorro = caja_ahorro + aux
    c = c + 1
    print(f"El {c}° año ahorraras {round(caja_ahorro, 2)}")

#Ejercicio 12
pan = 3.49
descuento = 0.6
pan_viejo = int(input("Cantidad de pan vendido que no es del dia: "))
descuento = (pan_viejo * pan) * descuento
precio_total = (pan_viejo * pan) - descuento
print(f"El precio del pan es de {pan}, el descuento es de {descuento} y el coste final es {round(precio_total, 3)}")