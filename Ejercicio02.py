#Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
import os
a = int(input('Escribe un numero entero que este entre el 1 y el 10'))
file = 'tabla' + str(a) + '.txt'
if os.path.isfile(file):
    x = open(file, 'r')
    print(x.read())
    x.close
else:
    print('No encontramos la tabla')
    