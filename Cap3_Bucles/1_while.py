
contador = 0

print('2 elevado a la ' + str(contador) + ' es: ' + str(2**contador))


def run():
    LIMITE = 10

    contador = 0
    potencia_2 = 2**contador

    while contador < LIMITE:
        print('2 elevado a la ' + str(contador) + ' es: ' + str(potencia_2))
        potencia_2 = 2**contador
        contador += 1
        # contador = contador + 1


if __name__ == '__main__':
    run()