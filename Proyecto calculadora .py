def sumar(general,verificador):
    print("¿Cuál opción quieres?")
    print("1. Solo hacer operación de suma")
    print("2. Hacer operación general con distintos signos")
    elección = int(input("Elige la opción: "))
    match elección:
        case 1:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
            numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
            suma = numero1 + numero2#Hace la operacion
            while True:
                respuesta = str(input("¿Quieres seguir sumando?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    print(f"La suma de los numeros es: {suma}")#Muestra el resultado de la suma
                    return general, verificador# Regresa los valores de estas dos variables
                
                print("Que ópción quieres?:")#Aqui eliges la opcion de la misma operacion por si no quieres salirte de esta operacion y 
                #seguir haciendo la misma operacion
                print("1.Agregar otro numero a la suma")
                print("2.Otra suma con diferentes variables ")
                opcion = int(input("Elige la opcion: "))
                match opcion:
                        case 1:
                            numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                            suma+= numero_extra#Hace otra suma
                            print(f"La suma de los numeros es: {suma}")#Muestra el resultado de la suma
                        case 2:
                            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
                            numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
                            suma = numero1 + numero2#Hace la operacion
                            print(f"La suma de los numeros es: {suma}")#Muestra el resultado de la suma
                        case _:
                            print("O kinezikano kalkulàtoro phenel kaj i opcia naj validno-Romani")
        case 2:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numer
            general+=numero1
            verificador+=1
            while True:
                respuesta = str(input("¿Quieres seguir sumando en la operacion general?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    return general, verificador # Regresa los valores de estas dos variables
                numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                general+= numero_extra#Hace otra suma
                verificador+=1
        case _:
            print("O kinezikano kalkulàtoro phenel kaj i opcia naj validno-Romani")
            return general, verificador # Regresa los valores de estas dos variables
            
 
def resta(general,verificador):
    print("¿Cuál opción quieres?")#Eliges opcion  
    print("1. Solo hacer operación de suma")
    print("2. Hacer operación general con distintos signos")
    elección = int(input("Elige la opción: "))
    match elección:
        case 1:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
            numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
            resta = numero1 - numero2#Hace la operacion
            while True:
                respuesta = str(input("¿Quieres seguir restando?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    print(f"La resta de los numeros es: {resta}")#Muestra el resultado de la resta
                    return general, verificador# Regresa los valores de estas dos variables
                
                print("Que ópción quieres?:")#Aqui eliges la opcion de la misma operacion por si no quieres salirte de esta operacion y 
                #seguir haciendo la misma operacion
                print("1.Resta otro numero a la operación")
                print("2.Otra resta con diferentes variables ")
                opcion = int(input("Elige la opcion: "))
                match opcion:
                        case 1:
                            numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                            resta-= numero_extra#Hace otra resta
                            print(f"La resta de los numeros es: {resta}")#Muestra el resultado de la resta
                        case 2:
                            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
                            numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
                            resta = numero1 - numero2#Hace la operacion
                            print(f"La resta de los numeros es: {resta}")#Muestra el resultado de la resta
                        case _:
                            print("Romani-Rechner meldet ungültige Option-Aleman")
        case 2:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numer
            general-=numero1
            verificador+=1
            while True:
                respuesta = str(input("¿Quieres seguir restando en la operacion general?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    return general, verificador # Regresa los valores de estas dos variables
                numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                general-= numero_extra#Hace otra resta
                verificador+=1
        case _:
            print("Romani-Rechner meldet ungültige Option-Aleman")
            return general, verificador # Regresa los valores de estas dos variables
            
def multiplicacion(general,verificador):
    print("¿Cuál opción quieres?")#Eliges opcion  
    print("1. Solo hacer operación de multiplicacion")
    print("2. Hacer operación general con distintos signos")
    elección = int(input("Elige la opción: "))
    match elección:
        case 1:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
            numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
            multiplicacion = numero1 * numero2#Hace la operacion
            while True:
                respuesta = str(input("¿Quieres seguir multiplicando?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    print(f"La multiplicacion de los numeros es: {multiplicacion}")#Muestra el resultado de la multiplicacion
                    return general, verificador# Regresa los valores de estas dos variables
                
                print("Que ópción quieres?:")#Aqui eliges la opcion de la misma operacion por si no quieres salirte de esta operacion y 
                #seguir haciendo la misma operacion
                print("1.Multiplicar a otro numero a la operación")
                print("2.Otra multiplicar con diferentes variables ")
                opcion = int(input("Elige la opcion: "))
                match opcion:
                        case 1:
                            numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                            multiplicacion*= numero_extra#Hace otra multiplicacion
                            print(f"La multiplicacion de los numeros es: {multiplicacion}")#Muestra el resultado de la multiplicacion
                        case 2:
                            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
                            numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
                            multiplicacion = numero1 * numero2#Hace la operacion
                            print(f"La multiplicación de los numeros es: {multiplicacion}")#Muestra el resultado de la sumultiplicacion
                        case _:
                            print("La calculatrice lettone indique une option invalide-Francés")
        case 2:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numer
            general*=numero1
            verificador+=1
            while True:
                respuesta = str(input("¿Quieres seguir multiplicando en la operacion general?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    return general, verificador # Regresa los valores de estas dos variables
                numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                general*= numero_extra#Hace otra resta
                verificador+=1
        case _:
            print("La calculatrice lettone indique une option invalide-Francés")
            return general, verificador # Regresa los valores de estas dos variables

def division(general,verificador):
    print("¿Cuál opción quieres?")#Eliges opcion  
    print("1. Solo hacer operación de dividir")
    print("2. Hacer operación general con distintos signos")
    elección = int(input("Elige la opción: "))
    match elección:
        case 1:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
            numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
            division = numero1 / numero2#Hace la operacion
            while True:
                respuesta = str(input("¿Quieres seguir dividiendo?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    print(f"La divison de los numeros es: {division}")#Muestra el resultado de la divison
                    return general, verificador# Regresa los valores de estas dos variables
                
                print("Que ópción quieres?:")#Aqui eliges la opcion de la misma operacion por si no quieres salirte de esta operacion y 
                #seguir haciendo la misma operacion
                print("1.Dividir a otro numero a la operación")
                print("2.Otra dividir con diferentes variables ")
                opcion = int(input("Elige la opcion: "))
                match opcion:
                        case 1:
                            numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                            division/= numero_extra#Hace operacion
                            print(f"La divison de los numeros es: {division}")#Muestra el resultado de la divison
                        case 2:
                            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
                            numero2 = float(input("Ingresa otro numero: "))#Pide la computadora al usuario el segundo numero
                            division = numero1 / numero2#Hace la operacion
                            print(f"La division de los numeros es: {division}")#Muestra el resultado de la division
                        case _:
                            print("Французский калькулятор говорит, что недопустимая опция-Rusa")
        case 2:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numer
            general/=numero1
            verificador+=1
            while True:
                respuesta = str(input("¿Quieres seguir multiplicando en la operacion general?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    return general, verificador # Regresa los valores de estas dos variables
                numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                general/= numero_extra#Hace otra operacion
                verificador+=1
        case _:
            print("Французский калькулятор говорит, что недопустимая опция-Rusa")
            return general, verificador # Regresa los valores de estas dos variables

def potencia(general,verificador):
    print("¿Cuál opción quieres?")#Eliges opcion  
    print("1. Solo hacer operación de potencias")
    print("2. Hacer operación general con distintos signos")
    elección = int(input("Elige la opción: "))
    match elección:
        case 1:
            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
            numero2 = float(input("Ingresa su potencia: "))#Pide la computadora al usuario el segundo numero
            potencia = numero1 ** numero2#Hace la operacion
            while True:
                respuesta = str(input("¿Quieres seguir elevando los numeros?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    print(f"El numero {numero1} con la potencia {numero2} su resultado es: {potencia}")#Muestra el resultado de la potencia
                    return general, verificador # Regresa los valores de estas dos variables
                print("Que ópción quieres?:")#Aqui eliges la opcion de la misma operacion por si no quieres salirte de esta operacion y 
                #seguir haciendo la misma operacion
                print("1.Hacer la potencia de otro numero a la operación")
                print("2.Otra pótencia con diferentes variables ")
                opcion = int(input("Elige la opcion: "))
                match opcion:
                        case 1:
                            numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                            potencia**= numero_extra#Hace operacion
                            print(f"El numero {potencia} con la potencia {numero_extra} su resultado es: {potencia}")#Muestra el resultado de la potencia
    
                        case 2:
                            numero1 = float(input("Ingresa un numero: "))#Pide la computadora al usuario te de el primer numero
                            numero2 = float(input("Ingresa su potencia: "))#Pide la computadora al usuario el segundo numero
                            potencia = numero1 / numero2#Hace la operacion
                            print(f"El numero {numero1} con la potencia {numero2} su resultado es: {potencia}")#Muestra el resultado de la potencia
                        case _:
                            print("俄罗斯计算器显示无效选项-China")
        case 2:
            numero1 = float(input("Ingresa una potencia: "))#Pide la computadora al usuario te de el primer numer
            general**=numero1
            verificador+=1
            while True:
                respuesta = str(input("¿Quieres seguir con otra potencia en la operacion general?: "))#Pregunta si quiere sumar otro numero si no rompe el bucle
                if respuesta == "No" or respuesta == "no" or respuesta == "N" or respuesta == "n" or respuesta == "NO":
                    return general, verificador # Regresa los valores de estas dos variables
                numero_extra = float(input("Ingresa otro numero: "))#Ingresa otro numero
                general**= numero_extra#Hace otra operacion
                verificador+=1
        case _:
            print("俄罗斯计算器显示无效选项-China")
            return general, verificador # Regresa los valores de estas dos variables
   
print("Calculadora\n")
print("Opciones de la calculadora: ")#Muestras opciones de la calculadora de las que puedes elegir
print("\n1.Suma")
print("\n2.Resta")
print("\n3.Multiplicacion")
print("\n4.Division")
print("\n5.Potencia")
general = 0 
verificador = 0#Esta revisa si hizo una operacion en general

while True: #Con este ciclo se repetira la opcion de elegir opciones
    numero_elegir = int(input("Elige una de las opciones: "))#En esta variable selecciona cualquiera de las opciones
    match numero_elegir:
        case 1:
           general,verificador = sumar(general,verificador)#Te manda a la funcion de suma
        case 2:
            general,verificador = resta(general,verificador)#Te manda a la funcion de resta
        case 3:
           general,verificador =  multiplicacion(general,verificador)#Te manda a la funvion de multiplicacion
        case 4: 
            general,verificador = division(general,verificador)#Te manda a la funcion de division
        case 5:
            general,verificador = potencia(general,verificador)#RTe mana la funcion de potencia
        case _:
            print("Opcion no valida")
    opcion = str(input("\nQuieres elegir otra vez alguna opcion: "))#Le pregunta al usurio si quiere seguir usando la calculadora
    #con sus funciones, si responde no termina el programa
    if opcion == "No" or opcion == "no" or opcion == "N" or opcion == "n"or opcion == "NO":
            if verificador > 0:
                print(f"La operacion final de general es: {general}")
            break
    else:
        print("No existe esta opcion")
