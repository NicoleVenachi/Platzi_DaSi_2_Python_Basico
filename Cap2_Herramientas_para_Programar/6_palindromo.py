# Saber si palabra son palindromos o no
# se leen igal al derecho y revés

def palindromo(palabra):
    # Primero limpio palabra. 
    # Paso todo a minusculas
    # Quito todos los espacios de la palabra
    #e.g., luz azul -> Luzazul

    palabra = palabra.replace(' ', '') 
    palabra = palabra.lower() 
    palabra_backwards = palabra[::-1]

    if palabra == palabra_backwards:
        return True
    else:
        return False


def run(): # funcion principal como entrada del proyecto
    palabra = input('Escirbe una palabra:   ')
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__': #Punto de entrada del proyecto
    run()


