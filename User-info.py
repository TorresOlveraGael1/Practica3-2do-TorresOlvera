#Preguntar al usuario nombre, edad, dirección y teléfono y lo guarde en un diccionario después debe mostrar por pantalla el mensaje 

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Crear un diccionario para almacenar la información del usuario
usuario = {
    'nombre' : ' ',
    'edad' : ' ',
    'direccion' : ' ',
    'telefono': ' '
}

#Solicitar información al usuario
usuario['nombre'] = input("Introduce tu nombre: ")
usuario['edad'] = input("Introduce tu edad: ")
usuario['direccion'] = input("Introduce tu dirección: ")
usuario['telefono'] = input("Introduce tu número de teléfono: ")

#Mostrar la información en el formato deseado
print(f"{usuario['nombre']}") 
print (f"tiene {usuario['edad']} años,")
print(f"vive en {usuario['direccion']}")
print (f"su número de teléfono es {usuario['telefono']}.")
