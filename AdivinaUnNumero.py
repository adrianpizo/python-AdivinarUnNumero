import random

def AdivinarUnNumero():
    #Generamos aleatoriamente (random) un numero entre 1 y 100
    numeroSecreto=random.randint(1,100)
    intentos=0
    Adivinado=False

    print('¡Bienvendo al juego de adivinanza de numero!')
    print('Intenta adivinar un numero entre 1 al 100')

    while not Adivinado:
        #Solicitar un numero del 1 al 100
        NumAdvinar=input('Ingresa un numero del 1 al 100: ')

        #Verificamos que la entrada (input) sea un numero
        if NumAdvinar.isdigit():
            NumAdvinar=int(NumAdvinar) #Pasamos de texto a entero
            intentos+=1

            if NumAdvinar > numeroSecreto:
                print(f'El número {NumAdvinar}, debe ser MENOR')
            elif NumAdvinar < numeroSecreto:
                print(f'El número {NumAdvinar}, debe ser MAYOR')
            else:
                print('FELICIDADES, HAZ ADVINADO EL NUMERO!!')
                print(f'El numero {NumAdvinar} es el secreto y lo lograste en {intentos} intentos')

        else:
            print('Debes ingresar un numero entero')

AdivinarUnNumero()