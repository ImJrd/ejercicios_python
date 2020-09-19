#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
num_hours = input("¿Cuantas horas trabaja al dia? ")
price = input("Valor de 1 hora: ")
pay = float(num_hours) * float(price)
print("Su pago del día es: " + str(pay))
