#Escribir un programa que muestre por pantalla la tabla de multiplicar indicada
n = int (input("Ingresa la tabla de multiplcar que deseas: "))
for i in range(0, 11):
    print(n,"*",i,"=", n*i)