cantidad = input('Digita la cantidad de COP a convertir: ')
cantidad = float(cantidad)

valor_dolar = 3875 # un dolar es cuantos pesos

cantidad_USD = cantidad / valor_dolar
cantidad_USD = round(cantidad_USD,2) #redondeo a 2 decimales
cantidad_USD = str(cantidad_USD)

print('Tienes $' + cantidad_USD + ' dólares')

