"""
# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un numero entero: "))
for i in range(numero):
    print(f"Tu nombre es {nombre} repetido {numero} veces")


# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces,
# una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
nombre2 = input("Ingrese su nombre completo: ")
print(nombre2.lower())
print(nombre2.upper())
print(nombre2.title())

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
nombre3 = input("Ingrese su nombre: ")
#n = 0
#for i in nombre3:
#    n += 1
#print(f"{nombre3.upper()} tiene {n} letras")
print(f"{nombre3.upper()} tiene {len(nombre3)} letras")

# Ejercicio 4
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
#Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])

# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
frase = str(input("Ingrese una frase: "))
frase_invertida = ""
for letra in frase:
    frase_invertida = letra + frase_invertida
print(frase_invertida)
print(frase[::-1])

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
frase = str(input("Ingrese una frase: "))
vocal = input("Ingrese una vocal en minuscula: ")
frase_convertida = ""
for i in frase:
    if i == vocal:
        frase_convertida = frase_convertida + vocal.upper()
    else:
        frase_convertida = frase_convertida + i
print(frase_convertida)
print(f"{frase.replace(vocal, vocal.upper())}")

# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
correo = str(input("Ingrese su correo electronico: "))
correo_nuevo = ""
#for i in correo:
#    if i == "@":
#        correo_nuevo = correo_nuevo + "@ceu.es"
#        break
#    else:
#        correo_nuevo = correo_nuevo + i
#print(correo_nuevo)
for i in correo[:correo.find("@")]:
    correo_nuevo = correo_nuevo + i
print(correo_nuevo + "@ceu.es")
print(correo[:correo.find('@')] + '@ceu.es')

# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de pesos y el número de céntimos del precio introducido.
#precio = input("Ingrese el precio del producto: ")
#print(f"El precio del producto es de {precio[:precio.find('.')]} pesos y {precio[precio.find('.')+1:]} centavos")
precio = float(input("Ingrese el precio del producto: "))
precioNuevo = str(precio)
pesos = ""
centavos = ""
for i in precioNuevo[:precioNuevo.find(".")]:
    pesos = pesos + i
for i in precioNuevo[precioNuevo.find(".")+1:]:
    centavos = centavos + i
print(f"{pesos} pesos y {centavos} centavos")

# Ejericio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
#fecha = input("Igrese la fecha de nacimiento dd/mm/aaaa: ")
#print(f"{fecha[:2]} dia")
#print(f"{fecha[3:5]} mes")
#print(f"{fecha[6:]} año")
from datetime import datetime

while True:
    try:
        fecha = input("Ingresa su fecha de nacimiento dd/mm/aaaa: ")
        datetime.strptime(fecha, '%d/%m/%Y')
        print("Fecha válida")
        print(f"Dia: {fecha[:2]}, Mes: {fecha[3:5]}, Año {fecha[6:]}")
        break
    except ValueError:
        print("Fecha inválida")

# Ejercicio 10
compras = str(input("Ingrese la lista de compras separadas por coma (1, 2, 3, ...): "))
l = compras.split(", ")
for i in l:
    print(i)


# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese su precio: "))
unidades = int(input("Ingrese la cantidad de unidades: "))
total = float(precio * unidades)
print(f"{producto}: {unidades:03d} unidades * {precio:.2f}$ = {total:.2f}$")
"""