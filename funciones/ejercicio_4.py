# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21 % .
def pago (cantidad, p_iva=21):
    total = (float(cantidad)*(float(p_iva)/100)) + float(cantidad)
    return total


# cantidad = input("Ingrese la cantidad total: ")
# iva = input("Ingrese el porcentaje de IVA: ")
# print(pago(cantidad, iva))
print(pago(1000, 16))
print(pago(1000))
