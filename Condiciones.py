"""
# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contra = "contraseña"
password = input("Ingrese la palabra contraseña: ")
if contra == password.lower():
    print("Coinciden las contraseñas")
else:
    print("No coinciden las contraseñas")

# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
total = None
nro1 = int(input("Ingrese un numero: "))
nro2 = int(input("Igrese otro numero: "))
try:
    total = nro1/nro2
except ArithmeticError as e:
    print(f"Ocurrio un error: {e}")

print(f"Resultado: {total}")

# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
nro = int(input("Ingrese un numero: "))
if nro % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")

# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Sus ingresos mensuales: "))
if edad >= 18 and ingresos >= 1000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")

# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
grupo = None
sexo = input("Ingrese su sexo (M o F): ")
nombre = input("Ingrese su nombre: ")
if sexo.upper() == "F":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
elif sexo.upper() == "M":
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
else:
    print("Sexo ingresado incorrecto")
print(f"Perteneces al grupo {grupo}")

# Ejercicio 7
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	                Tipo impositivo
# Menos de 10000€	        5%
# Entre 10000€ y 20000€	    15%
# Entre 20000€ y 35000€	    20%
# Entre 35000€ y 60000€	    30%
# Más de 60000€	            45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
renta = int(input("Ingrese su renta anual: "))
impositivo = None
if renta > 60000:
    impositivo = 0.45
elif renta <= 60000 and renta > 35000:
    impositivo = 0.30
elif renta <= 35000 and renta > 20000:
    impositivo = 0.20
elif renta <= 20000 and renta >= 10000:
    impositivo = 0.15
else:
    impositivo = 0.05
total = renta * impositivo
print(f"Usted tiene que pagar un monto de {total:.2f}$")

# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel	        Puntuación
# Inaceptable	    0.0
# Aceptable	        0.4
# Meritorio     	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
puntuacion = float(input("Ingrese su puntuacion: "))
nivel = None
dinero = 2400 * puntuacion
if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    dinero = 0
if dinero == 0:
    print("Valor incorrecto... ")
else:
    print(f"Su nivel es {nivel} y la cantidad de dinero a recibir es {dinero}$")

# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("El precio de la entrada es de 10$")
elif 4 <= edad <= 18:
    print("El precio de la entrada es de 5$")
else:
    print("El precio de la entrada es gratis")
"""
# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
def vegetariana(opcion):
    ingredientes = None
    if opcion == 1:
        ingredientes = "Pimiento"
    elif opcion == 2:
        ingredientes = "Tofu"
    else:
        print("Opcion incorrecta")
    return print(f"Pizza vegetariana con mozzarella, tomate y {ingredientes}")

def noVegetariana(opcion):
    ingredientes = None
    if opcion == 1:
        ingredientes = "Peperoni"
    elif opcion == 2:
        ingredientes = "Jamon"
    elif opcion == 3:
        ingredientes = "Salmon"
    else:
        print("Opcion incorrecta")
    return print(f"Pizza No Vegetariana con mozzarella, tomate y {ingredientes}")

opcion = None
while opcion != 0:
    try:
        print("Pizzeria Bella Napoli".center(30, "-"))
        print("1 - Pizza Vegetariana")
        print("2 - Pizza No Vegeteraniana")
        print("0 - Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            print("Ingredientes a elegir".center(30, "-"))
            print("1)Pimiento")
            print("2)Tofu")
            opc_ingredientes = int(input("Elija una opcion de ingrediente: "))
            vegetariana(opc_ingredientes)
        elif opcion == 2:
            print("Ingredientes a elegir".center(30, "-"))
            print("1)Peperoni")
            print("2)Jamon")
            print("2)Salmon")
            opc_ingredientes = int(input("Elija una opcion de ingrediente: "))
            noVegetariana(opc_ingredientes)
        elif opcion > 2:
            print("Opcion incorrecta, elija otra...")

    except Exception as e:
        print(f"Ocurrio un error {e}")
        opcion = None
else:
    print("Salimos del programa...")
