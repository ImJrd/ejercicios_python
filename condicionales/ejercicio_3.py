#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
number_one = input("Ingrese el 1 numero: ")
number_two = input("Ingrese el 2 numero: ")
div = float(number_one)/float(number_two)
if float(number_one) == 0:
    print("Error")
else:
    print("El resultado de la división es: " + str(div))
