#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
qty = input("Ingrese la cantidad a invertir: ")
interest = input("Ingrese el interes anual: ")
no_years = input("Años de la inversión: ")
for i in range(1, int(no_years)+1):
    it = float(qty)*((float(interest)/100)*(float(i)))
    capital = float(qty) + it
    print("Su capital en el año", i, "es de $", capital)
