#Escribir un programa que lea un entero positivo,n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta .
number = input("Ingrese un numero entero: ")
sum = (int(number)*(int(number)+1)/2)
print("La suma de los n primeros enteros positivos de " + number +" es: " + str(int(sum)))
