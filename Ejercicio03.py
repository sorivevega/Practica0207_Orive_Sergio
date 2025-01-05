#Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import os
n = int(input('Escribe un numero entero que este entre el 1 y el 10'))
m = int(input('Escribe un numero entero que este entre el 1 y el 10'))
file = 'tabla-' + str(n) + '.txt'

if os.path.isfile(file):
    x = open(file, 'r')
    y = x.readlines()
    print(y)
    z = y[m]
    print(z)
    x.close()
else:
    print('No existe')