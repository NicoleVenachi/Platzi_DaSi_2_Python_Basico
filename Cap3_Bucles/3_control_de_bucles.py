
def run():

    for contador in range(10):

        if ((contador % 2) != 0):
            continue
            # Para impares, va a ste ejecucion
        elif contador == 7:
            break
        else:
            pass

        print(contador)
        # Solo imprimira pares

    texto = input('Escribre un texto: ')

    for caracter in texto:
        if(caracter == 'o'):
            break
            ## si recibo una 'o', me salgo
        else:
            print(caracter)


if __name__ == '__main__':
    run()
