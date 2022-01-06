
menu = ''' 
    Bienvenido al conversor de monedas 💲
       1. Pesos Colombianos
       2. Pesos Argentos
       3. Pesos Mexas
    Elige una opción: '''
opcion = int(input(menu))

if opcion == 1:
    cantidad = input('Digita la cantidad de COP a convertir: ')
    cantidad = float(cantidad)
    valor_dolar = 3875 # un dolar es cuantos COP es

elif opcion == 2:
    
    cantidad = input('Digita la cantidad de ARP a convertir: ')
    cantidad = float(cantidad)
    valor_dolar = 65 # un dolar es cuantos ARP es

elif opcion == 3:
    cantidad = input('Digita la cantidad de MXN a convertir: ')
    cantidad = float(cantidad)
    valor_dolar = 24 # un dolar es cuantos MXN es

else:
    print('No sea tan mk, opcion invalida')
    exit() #Si elije opcion invalida, me salgo


cantidad_USD = cantidad / valor_dolar
cantidad_USD = round(cantidad_USD,2) #redondeo a 2 decimales
cantidad_USD = str(cantidad_USD)

print('Tienes $' + cantidad_USD + ' dólares')



