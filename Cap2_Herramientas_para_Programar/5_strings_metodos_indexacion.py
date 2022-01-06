
nombre = 'nicole   '
nombre.upper() 
# NICOLE____
nombre.capitalize()
# Nicole_____
nombre.lower()
# nicole_____
nombre.strip()
# nicole
nombre.strip('ni')
# cole______
nombre.replace('o', 'x')
# nicxle
nombre.find('ol')
# 3
nombre.startswith('ju')
# False
nombre.endswith('   ')
# True


len(nombre)
# 6

fist_letter = nombre[0]
# n

#Slices

nombre[1:4]
# ico
nombre[0:6:2]
# ncl
nombre[::]
# string completo
nombre[::-1]
# _____elocin

#splits

nombre.split('ol')
# ['nic', 'e_____']

# join
contrasena = ''.join([1, 2, 3])
contrasena = '#'.join([1, 2, 3])
# 123
# 1#2#3