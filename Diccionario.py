#El usuario debe meter una divisa y debe mostrar el símbolo o un mensaje de que la divisa no está en el diccionario.

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definir el diccionario con las divisas y sus símbolos
divisas = {
    'Euro': '€', 
    'Dollar': '$', 
    'Yen': '¥'
}

#Solicitar al usuario que ingrese una divisa
divisa_usuario = input("Introduce una divisa (Euro, Dollar, Yen): ")

#Verificar si la divisa está en el diccionario y mostrar el símbolo o un mensaje
if divisa_usuario in divisas:
    print(f"El símbolo de {divisa_usuario} es: {divisas[divisa_usuario]}")
else:
    print("La divisa no está en el diccionario.")
