#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
n = input("Ingrese un numero entero positivo: ")
for i in range(0, int(n)+1):
    print(i, end=",")