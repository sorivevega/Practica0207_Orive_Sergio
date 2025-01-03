#Escribir un programa que acceda al fichero de internet mediante la url indicada y muestre por pantalla el número de palabras que contiene.
#http://textfiles.com/adventure/aencounter.txt 

import urllib.request

url = 'http://textfiles.com/adventure/aencounter.txt' 
file = urllib.request.urlopen(url)
for line in file:
    decode_line = line.decode('utf-8')
    print(decode_line)

texto = decode_line
numero = texto.split()
palabras = len(numero)
print (palabras)