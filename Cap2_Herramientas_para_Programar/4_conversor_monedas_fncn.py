
def conversor(valor_dolar, tipo_pesos):
    cantidad = input('Digita la cantidad de ' + tipo_pesos + 'a convertir: ')
    cantidad = float(cantidad)

    cantidad_USD = cantidad / valor_dolar
    cantidad_USD = round(cantidad_USD,2) #redondeo a 2 decimales
    cantidad_USD = str(cantidad_USD)

    return cantidad_USD

menu = ''' 
    Bienvenido al conversor de monedas 💲
       1. Pesos Colombianos
       2. Pesos Argentos
       3. Pesos Mexas
    Elige una opción: '''
opcion = int(input(menu))


if opcion == 1:

    cantidad_USD = conversor(3875, 'COP')
    # un dolar es cuantos COP es

elif opcion == 2:
    
    cantidad_USD = conversor(65, 'ARP')

elif opcion == 3:

    cantidad_USD = conversor(24, 'MXN')

else:
    print('No sea tan mk, opcion invalida')
    exit() #Si elije opcion invalida, me salgo


print('Tienes $' + cantidad_USD + ' dólares')
