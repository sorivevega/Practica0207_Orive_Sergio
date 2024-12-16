#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
def Multiplicaciones ():
    number = int(input('Introduzca un numero: '))
    n = 0
    texto = ('tabla' + str(number)+ 'txt')
    file = open(texto, 'w' )
    
    while n <= 10: 
        operacion = str(number * n)
        n = n + 1
        print(operacion)
        file.write(operacion + '\n')
    file.close()
    
Multiplicaciones()