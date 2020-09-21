#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
cadena = input("Ingresar una palabra: ")
if str(cadena) == str(cadena)[::-1]:
    print("Es un palindromo")
else:
    print("No es un palindromo")
