#Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa debe  incorporar funciones para crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
import os

print('1, Añadir telefono')
print('2, Ver listado')
print('3, Eliminar telefono de la lista')
print('4, Terminar')
menu = (input('Que desea hacer'))

while menu != '4':

    if menu == '1':
        lista = input('Introduce el nombre del cliente y su telefono separado por comas')
        file = open('listin.txt', 'w') 
        file.write(lista)
        file.close()
    if menu == '2':
        os.listdir(file)
    if menu == '3':
        datos = input('Introduce el nombre del cliente y su telefono separado por comas que quieras eliminar de la lista')
        if datos in file:
            with open('listin.txt', 'w') as file:
                for linea in lista:
                    if linea.strip() == datos:
                        file.write(linea)
        print('Informacion eliminada')        
        
    if menu == '4':
        print('Adios')