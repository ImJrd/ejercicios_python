#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
interes = 0.04
cantidad_inicial = input("Ingrese la cantidad de dinero a depositar en la cuenta de ahorros: ")
ahorro_1 = ((float(cantidad_inicial)*interes)*1)+float(cantidad_inicial)
ahorro_2 = ((float(cantidad_inicial)*interes)*2)+float(cantidad_inicial)
ahorro_3 = ((float(cantidad_inicial)*interes)*3)+float(cantidad_inicial)
print("Sus ahorros en el 1 año son de $" + str(round(ahorro_1, 2)) + "\nSus ahorros en el 1 año son de $" + str(round(ahorro_2, 2)) + "\nSus ahorros en el 3 año son de $" + str(round(ahorro_3, 2)))


