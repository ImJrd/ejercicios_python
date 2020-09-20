#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra = input("Ingrese una palabra: ")
print("La vocal a aparece " + str(palabra.count("a")) + "\nLa vocal e aparece " + str(palabra.count("e")) + "\nLa vocal i aparece " + str(palabra.count("i")) + "\nLa vocal o aparece " + str(palabra.count("o")) + "\nLa vocal u aparece " + str(palabra.count("u")))
