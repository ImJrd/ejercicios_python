#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
datos_usuario = {
    "nombre":"",
    "edad":"",
    "direccion":"",
    "telefono":""
}
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
dirreccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su telefono: ")

datos_usuario["nombre"] = nombre
datos_usuario["edad"] = edad
datos_usuario["direccion"] = dirreccion
datos_usuario["telefono"] = telefono

print(datos_usuario["nombre"], "tiene", datos_usuario["edad"], "años, vive en",datos_usuario["direccion"], "y su número de teléfono es", datos_usuario["telefono"])
