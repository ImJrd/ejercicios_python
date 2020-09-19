#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
precio_pan = 3.49
barras_noday = input("Ingrese el numero de barras de pan vendidas que no son del dia: ")
coste = ((float(barras_noday)*precio_pan)*60)/100
print("El precion normal de una barra de pan es de " + str(precio_pan) + "€ c/u \nEl descuento por no ser fresca es el del 60% \nEl coste final es de " + str(round(coste, 2)) + "€")
