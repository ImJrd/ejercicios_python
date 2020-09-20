#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = input("Ingresa tu edad: ")
c = 1
while c <= int(edad):
    print(c, "año(s)")
    c = c + 1
