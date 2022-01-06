import random

def generar_contrasena():
    MAYUSCULAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    MINUSCULAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    SIMBOLOS = ['!', '#', '%', '$', '/', '(', ')']
    NUMEROS = ['1', '2', '3', '4', '5', '6', '7']

    caracteres = MAYUSCULAS + MINUSCULAS + SIMBOLOS + NUMEROS

    contrasena = []

    for element in range(15): # password de 15 caracteres
        caracter_random = random.choice(caracteres) # elige un caracter al azar
        contrasena.append(caracter_random)
    
    contrasena = ''.join(contrasena)

    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)


if __name__ == '__main__':
    run()