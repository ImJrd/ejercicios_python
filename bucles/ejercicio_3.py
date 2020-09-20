#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número.
n = int (input("Ingrese un numero entero positivo: "))
c = int (1)
while c <= n:
    if c%2 != 0:
        print(c, end=",")
    c = c + 1
