#Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial(numero):
    c = 1
    for i in range(numero):
        c *= i+1
    return c

n = int(input("Ingrese un numero entero: "))
print("El factorial de", n, "es " + str(factorial(n)))
