# ----------------------------------------------------------------------------
# PYTHON 3 - APUNTES Y EJEMPLOS
# Ejemplo: adivinar el número
# ----------------------------------------------------------------------------
# Autor: Juan Ocaña Valenzuela
# GitHub: patchispatch
# Este documento está regulado por la licencia GNU General Public License v3.0
# ----------------------------------------------------------------------------

# Este ejemplo consistirá en programar un juego de adivinar el número.
# El programa se presentará, "pensará" un número en un intervalo, y el jugador
# intentará adivinarlo, mientras el programa proporciona información sobre si 
# la entrada es demasiado grande o pequeña.

# ----------------------------------------------------------------------------

# Para empezar, debemos importar el módulo que nos permite generar números 
# aleatorios:
import random

# # Primero, el programa "pensará" un número entero entre 0 y 99:
# number = random.randint(0, 99)

# # Después, el bot se presentará:
# print("He pensado un número entre 0 y 99; ¿serás capaz de adivinarlo?")

# El juego consistirá en un bucle infinito, en el cual el usuario introducirá 
# un número, y el bot responderá si es mayor, menor, o igual al que pensó.
# En este último caso, el juego finalizará.

# # Sin funciones:

# while True:
#     n = input("Introduce un número entre 0 y 99: ")

#     # Se comprueba que es un número, y que está en el rango posible
#     try:
#         n = int(n)
#     except:
#         pass
#     else:
#         if not 0 <= n <= 99:
#             print("Creo que el juego no funciona así.")
#             break

#     # Por último, se comprueba si hemos acertado o no:
#     if n == number:
#         print("¡Has acertado!")
#         break
#     elif n < number:
#         print("¡Demasiado pequeño!")
#     else:
#         print("¡Demasiado grande!")

# Este ejemplo, que se halla comentado, es una forma de realizar el juego.
# Sin embargo, vamos a proceder a realizarlo con funciones:

# Variables globales para todo el script:
inicio = 0
fin = 99

# ----------------------------------------------------------------------------
# Funciones:

# Esta función establecerá el rango de números, y "pensará" el número a
# adivinar:
def inicio_juego():

    # Indicamos a Python que vamos a utilizar las variables del script,
    # y no unas locales a la función:
    global inicio
    global fin

    inicio = input("Introduce el inicio del intervalo: ")
    fin = input("Introduce el fin del intervalo: ")

    try:
        inicio = int(inicio)
        fin = int(fin)
    except:
        inicio = 0
        fin = 99

    print("De acuerdo, elegiré un número entre ", inicio, " y ", fin, ".")
    numero = random.randint(inicio, fin)

    return numero

# Esta función pedirá al usuario que introduzca un número en el rango de
# valores: 
def piensa_numero():

    global inicio
    global fin

    while True:
        
        # Nota: input() no deja poner comas como print().
        invitacion = "Piensa un número entre " + str(inicio) + " y " + str(fin) + ": "
        n = input(invitacion)
        try:
            n = int(n)
        except:
            pass
        else:
            if inicio <= n <= fin:
                break
        
    return n

# ----------------------------------------------------------------------------
# Main:

# Inicio del juego (generación aleatorio):
numero = inicio_juego()

# Proceso de adivinación:
adivinado = False
while not adivinado:

    # Solicitud al usuario:
    intento = piensa_numero()

    # Comprobación:
    if intento < numero:
        print("¡Demasiado pequeño! \n")
    elif intento > numero:
        print("¡Demasiado grande! \n")
    else:
        print("¡Has ganado!")
        adivinado = True

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------




        
    

