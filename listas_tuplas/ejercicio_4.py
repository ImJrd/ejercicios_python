#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
numeros_g = []
numero = input("Cantidad de numeros ganadores ")
for x in range(int(numero)):
    valor = int(input("Ingrese el numero ganador "))
    numeros_g.append(valor)
numeros_g.sort()
print(numeros_g)
