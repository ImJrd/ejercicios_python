interes = 0.04
cantidad_inicial = input("Ingrese la cantidad de dinero a depositar en la cuenta de ahorros: ")
ahorro_1 = ((float(cantidad_inicial)*interes)*1)+float(cantidad_inicial)
ahorro_2 = ((float(cantidad_inicial)*interes)*2)+float(cantidad_inicial)
ahorro_3 = ((float(cantidad_inicial)*interes)*3)+float(cantidad_inicial)
print("Sus ahorros en el 1 año son de $" + str(round(ahorro_1, 2)) + "\nSus ahorros en el 1 año son de $" + str(round(ahorro_2, 2)) + "\nSus ahorros en el 3 año son de $" + str(round(ahorro_3, 2)))


