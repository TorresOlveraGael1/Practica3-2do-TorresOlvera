#Guardar en un diccionario precios de las frutas en una matriz, luego preguntar al usuario por fruta 

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definir un diccionario con los precios de las frutas
precios_frutas = {
    'manzana': 2.5,  #precio por kilo
    'banana': 1.2,
    'naranja': 3.0,
    'uva': 4.0,
    'fresa': 5.5
}

#Preguntar al usuario por la fruta y la cantidad de kilos
fruta = input("Introduce la fruta que deseas comprar: ").lower()
kilos = float(input("Introduce el número de kilos: "))

#Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total:.2f} €")
else:
    print("La fruta no está en el diccionario.")
