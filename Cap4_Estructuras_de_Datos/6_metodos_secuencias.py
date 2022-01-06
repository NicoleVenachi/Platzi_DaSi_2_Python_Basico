objetos = [1, 'hola', True, 'hola']

# ------ Slices  ------
# (No existe en dicts)

objetos[::2]
objetos[::-1]
# [1, True]
# ['hola', True, 'hola', 1]

# ------ Metodos ------

objetos.index(True)
# 2
objetos.count('hola')
# 2

# --- Build-in-Fnctns ---
del objetos[2]
# [1, 'hola', 'hola]

for key, value in enumerate(objetos):
    print(key, value)
# 0 1     1 hola      2 True


# ----- Extras ------
objetos.index(True)
# 2
objetos[2] # no aplica 
# True
