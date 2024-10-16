# Practica3-2do-TorresOlvera

Torres Olvera Gael

En esta actividad realizamos un conjunto de codigos que nos solicitaron

# Punto 1

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

![image](https://github.com/user-attachments/assets/9da5ed90-f761-4cd2-81a7-17a1fc9a750c)
![image](https://github.com/user-attachments/assets/0250941f-b1b9-4ef0-8297-dcf5303eace3)
![image](https://github.com/user-attachments/assets/d34fe01a-662e-4189-8ab1-13e1bed7e072)


# Punto 2

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

![image](https://github.com/user-attachments/assets/a610fd55-3576-4a68-9986-a818f84a7bc1)
