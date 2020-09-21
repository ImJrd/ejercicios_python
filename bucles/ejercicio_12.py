#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
word = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")
print("La letra", letra, "aparece", word.count(letra), "veces en la palabra", word)
