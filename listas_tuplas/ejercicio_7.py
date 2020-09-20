#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
import string
letras = list(string.ascii_uppercase)

x = -1
for i in letras:
	x = x+1
	if (x % 2) == 0:
		letras.remove(i)
print(letras)




    
    
