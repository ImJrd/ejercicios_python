#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n1 = input("Ingresar el primer numero: ")
n2 = input("Ingresar el segundo numero: ")
c = float(n1)/float(n2)
r = float(n1)%float(n2)
print("La division de " + str(n1) + " entre " + str(n2) + " da un cociente de: " + str(c) + " y un residuo de " + str(r))
