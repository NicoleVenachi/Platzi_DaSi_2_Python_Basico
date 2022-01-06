# Verificar numeros primos
# se dividen solo entre sí y el 1
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1): # Divido de 1 hasta el numero
        if ((i==1) or (i==numero)): 
            continue #Ya se que por si mismo y 1 se dividen
        elif ((numero % i ) == 0):
            # si no es primo, acabo de contar
            contador += 1
            break
        else: # si modulo no es 0, sgte comprobacion
            continue
    if contador == 0:
        return True
    else:
        return False
            

def run():
    numero = int(input('Escribe un número:  '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()
