#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
palabra = "contraseña"
p = input("Introducir la contraseña: ")
if p == palabra.lower() or p == palabra.upper():
    print("La contraseña es correcta.")
else:
    print("Contraseña incorrecta.")
