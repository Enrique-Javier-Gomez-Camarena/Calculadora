# Calculadora
<h2> Calculadora básica en python </h2>
##Descripción del proyecto
Este proyecto es una calculadora interactiva en Python que permite realizar operaciones matemáticas básicas como suma, resta, multiplicación, división y potencias. El usuario puede elegir la operación que desea realizar y se le permite seguir operando con más números si así lo desea. El programa sigue funcionando hasta que el usuario decide salir.
##Lista de funcionalidades implementadas
Menú interactivo: Permite al usuario seleccionar qué operación desea realizar.

Suma: Permite sumar dos o más números.

Resta: Permite restar dos o más números en cadena.

Multiplicación: Permite multiplicar dos o más números.

División: Realiza divisiones y permite hacer más de una operación.

Potencia: Calcula potencias de un número elevado a otro.

Repetición de operaciones: Después de cada operación, se pregunta al usuario si desea realizar otra.

Validación básica de entrada: Repite el menú si el usuario ingresa una opción inválida.
def sumar():
    numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
    numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
    suma = numero1 + numero2#Hace la operacion
    while True:
        respuesta = str(input("¿Quieres sumar un numero extra: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
        if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
            break
        numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
        suma+= numero_extra#Hace otra suma
    print(f"La suma de los numeros es: {suma}")#Muestra el resultado de la suma

def resta():
    numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
    numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
    resta = numero1 - numero2#Hace la operacion
    while True:
        respuesta = str(input("¿Quieres restar un numero extra: "))#Pregunta si quiere restar otro numero si no rompe el bucle
        if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
            break
        numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
        resta-= numero_extra#Hace la operacion
    print(f"La resta de los numeros es: {resta}")#Muestra el resultado de la resta

def multiplicacion():
    numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
    numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
    multiplicacion = numero1 * numero2#Hace la operacion
    while True:
        respuesta = str(input("¿Quieres multiplicar un numero extra: "))#Pregunta si quiere multiplicar otro numero si no rompe el bucle
        if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
            break
        numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
        multiplicacion*= numero_extra#Hace la operacion
    print(f"La multiplicacion de los numeros es: {multiplicacion}")#Muestra el resultado de la multiplicacion 

def division():
    numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
    numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
    divison = numero1 / numero2#Hace la operacion
    print(f"La division de los numeros es: {division}")#Muestra el resultado de la division
    while True:
        respuesta = str(input("¿Quieres dividir otra vez: "))#Pregunta si quiere dividir otra vez si no rompe el bucle
        if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
            break
        numero1 = float(input("Ingresa un numero: "))#Ingresa otro numero
        numero2 = float(input("Ingresa otro numero: "))#Despues pide otro numero para la operacion
        divison = numero1 / numero2#Hace la operacion
        print(f"La division de los numeros es: {division}")#Muestra el resultado de la division
    

def potencia():
    numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
    numero2 = float(input("Ingresa su potencia: "))#Pide la computadora al usuario el segundo numero
    potencia = numero1**numero2#Hace la operacion
    print(f"El numero {numero1} con la potencia {numero2} su resultado es: {potencia}")#Muestra el resultado de la potencia
    while True:
        respuesta = str(input("¿Quieres hacer otra potencia? "))#Pregunta si quiere hacer otra potencia si no rompe el bucle
        if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
            break
        numero1 = float(input("Ingresa un numero: "))#Ingresa otro numero
        numero2 = float(input("Ingresa su potencia: "))#Despues pide otro numero para la operacion
        potencia = numero1**numero2#Hace la operacion
        print(f"El numero {numero1} con la potencia {numero2} su resultado es: {potencia}")#Muestra el resultado de la potencia
    

print("Opciones de la calculadora: ")#Muestras opciones de la calculadora de las que puedes elegir
print("\n1.Suma")
print("\n2.Resta")
print("\n3.Multiplicacion")
print("\n4.Division")
print("\n5.Potencia")

numero_elegir = int(input("Elige una de las opciones: "))#En esta variable selecciona cualquiera de las opciones

while True: #Con este ciclo se repetira la opcion de elegir opciones
    match numero_elegir:
        case 1:
            sumar()#Te manda a la funcion de suma
        case 2:
            resta()#Te manda a la funcion de resta
        case 3:
            multiplicacion()#Te manda a la funvion de multiplicacion
        case 4: 
            division()#Te manda a la funcion de division
        case 5:
            potencia()#RTe mana la funcion de potencia
        case _:
            print("Opcion no valida")
    opcion = str(input("\nQuieres elegir otra vez alguna opcion: "))#Le pregunta al usurio si quiere seguir usando la calculadora
    #con sus funciones, si responde no termina el programa
    if opcion == "No" or opcion == "no" or opcion == "N" or opcion == "n"or opcion == "NO":
            break
    elif opcion == "Si" or opcion == "si" or opcion == "S" or opcion == "s" or opcion == "SI":
        numero_elegir = int(input("Elige una de las opciones: "))
