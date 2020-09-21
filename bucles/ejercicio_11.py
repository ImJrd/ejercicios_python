#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
w = input("Ingrese una palabra: ")
w_rev = '\n'.join(reversed(w))
print(w_rev)
