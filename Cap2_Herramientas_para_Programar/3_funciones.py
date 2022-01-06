# Si quisiera imprimirlo 3 veces

# print('Mensaje especial:   ')
# print('Estoy aprendiendo a usar funciones!')
# print('Mensaje especial:   ')
# print('Estoy aprendiendo a usar funciones!')
# print('Mensaje especial:   ')
# print('Estoy aprendiendo a usar funciones!')

def imprimir_mensaje():
    print('Mensaje especial:   ')
    print('Estoy aprendiendo a usar funciones!')

# si deseo imprimirlo 3 veces, solo lo invoco 
# las 3 veces

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

# Fnciones con paramaetros

opcion = int(input('Elige una opción (1,2,3):   '))

def conversacion(mensaje):
    print('Hola, Cómo estás')
    print(mensaje)
    print('Adiós')

if opcion == 1:
    conversacion('Elegista la opción 1')

elif opcion == 2:
    conversacion('Elegista la opción 2')

elif opcion == 3:
    conversacion('Elegista la opción 3')

else:
    print('Opción invalida')

def suma(a,b):
    print("se suman dos números")
    resultado = a + b

    return resultado

print(suma(1,4))


