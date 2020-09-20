#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
renta_anual = input("Ingresa el total de la renta anual: ")
if float(renta_anual) < 10000:
    print("Tipo impostivo de 5%")
elif float(renta_anual) >= 10000 and float(renta_anual) < 20000:
    print("Tipo impostivo de 15%")
elif float(renta_anual) >= 20000 and float(renta_anual) < 35000:
    print("Tipo impostivo de 20%")
elif float(renta_anual) >= 35000 and float(renta_anual) < 60000:
    print("Tipo impostivo de 30%")
elif float(renta_anual) >= 60000:
    print("Tipo impostivo de 45%")
