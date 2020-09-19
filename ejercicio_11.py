#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
qty = input("Ingrese la cantidad a invertir: ")
interest = input("Ingrese el interes anual: ")
no_years = input("Años de la inversión: ")
return_qty = float(qty)*((float(interest)/100)*(float(no_years)))
capital = float(qty) + return_qty
print("Su capital al final sera de $" + str(round(capital, 2)))

