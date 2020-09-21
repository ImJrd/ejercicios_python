#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
s = "salir"
word = ""
while word != s:
    word = input("Ingrese una palabra: ")
    print(word)
