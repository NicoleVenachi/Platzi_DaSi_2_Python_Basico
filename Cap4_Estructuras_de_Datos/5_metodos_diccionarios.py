poblacion_paises = {
    'Argentina': 4493877,
    'Brasil': 210147125,
    'Colombia': 50372424
}

poblacion_paises.keys()
# [(Argentina, Colombia, Brasil)]

poblacion_paises.values()
# [(4493877, 210147125, 50372424)]

poblacion_paises.items()
# Por items: ([('Argentina', 4493877), 
# ('Brasil', 210147125), ('Colombia', 50372424)])

poblacion_paises.get('Puerto Rico', {'Pr': 2000000})
# {'Pr': 2000000}

#Agregar nuevos elementos:
poblacion_paises['Puerto Rico'] = 2000000