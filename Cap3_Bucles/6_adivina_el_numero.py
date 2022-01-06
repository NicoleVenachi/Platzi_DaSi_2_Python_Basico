# Computadora elige numero aleatorio y tenemos que adivinarloo
import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    
    while numero_aleatorio != numero_elegido:

        if numero_aleatorio > numero_elegido:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')

        numero_elegido = int(input("Elige otro número: "))
    print('Ganaste') # si son iguales, sale del while y gana

if __name__ == '__main__': 
    run()
    