#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def square_number(number):
    list = []
    for i in number:
        list.append(i**2)
    return list

print(square_number([1, 2, 3, 4, 5]))
