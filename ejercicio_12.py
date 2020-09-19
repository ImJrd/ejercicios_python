#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
kg_muñeca = 0.075
kg_payaso = 0.112
print("Jugueteria El Jockercito")
qty_muñecas = input("Ingresar el numero de muñecas a incluir en el paquete: ")
qty_payasos = input("Ingresar el numero de payasos a incluir en el paquete: ")
peso_paquete = (int(qty_muñecas)*kg_muñeca)+(int(qty_payasos)*kg_payaso)
print("El peso total del paquete es de " + str(peso_paquete) + "kg")
