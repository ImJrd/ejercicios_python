#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
divisa = {
    'Euro': '€', 
    'Dollar': '$', 
    'Yen': '¥'
}
r = input("Ingrese una divisa: ")
print(divisa.get(r.title(), "Divisa no encontrada"))



