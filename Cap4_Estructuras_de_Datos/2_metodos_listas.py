
letras = ['a', 'b', 'c', 'd']

letras.pop()
letras.pop(1)
# ['a', 'b', 'c']
# ['a', 'c']
letras.remove('a')
# ['c']

letras.append('b')
# ['c', 'b']

letras.sort()
# ['b', 'c']

import copy
letras_copia = copy.copy(letras)


