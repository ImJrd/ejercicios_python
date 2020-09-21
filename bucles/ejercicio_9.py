#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
pwd = str("contraseña")
pwd_1 = ""
while pwd_1 != pwd:
    pwd_1 = input("Ingrese la contraseña: ")
print("Contraseña correcta")
