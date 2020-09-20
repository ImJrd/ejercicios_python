#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad = input("Ingresa tu edad: ")
ingreso_mes= input("Ingresa tu total de ingresos mensuales: ")
if int(edad) > 16 and float(ingreso_mes) >= 1000:
    print("Usted debe tributar")
else:
    print("Aún no puede tributar")
