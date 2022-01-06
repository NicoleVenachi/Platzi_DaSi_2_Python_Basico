
    # mi_diccionario_a = {
    #     'llave_1': 1,
    #     'llave_2': 3,
    #     'llave_3': 3,
    # }
    # mi_diccionario_b = dict(llave_1 = 1, llave_2 = 2, llave_3 = 3)
    # # {'llave_1': 1, 'llave_2': 2, 'llave_3': 3}
    # print(mi_diccionario_a['llave_1'])

def run():
    #crear
    poblacion_paises = {
        'Argentina': 4493877,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    #recorrer
    
    #Por keys (Argentina, Colombia, Brasil)

    for pais in poblacion_paises.keys():
        print(pais)

    #Por keys ( 4493877, 210147125, 50372424)

    for poblacion in poblacion_paises.values():
        print(poblacion)

    #Por items: ('Argentina': 4493877, 'Brasil': 210147125, 'Colombia': 50372424)

    for pais, poblacion in poblacion_paises.items():
        print(pais, poblacion)


if __name__ == '__main__':
    run()
