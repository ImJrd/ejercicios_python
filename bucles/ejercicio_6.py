# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo, de altura el número introducido.
numero = int (input("Inidca un numero: "))
for i in range(1, numero + 1):
    print("*"*i)