#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
grupo_a_mujeres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
grupo_a_hombres = ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nombre = input("Ingresa tu primer nombre: ")
sexo = input("Ingresar su sexo (M/F): ")

if sexo == "F":
    for i in grupo_a_mujeres:
        if nombre.startswith(i):
            print("Hola", nombre, "perteneces al grupo A")
        else:
            print("Hola", nombre, "perteneces al grupo B")
        break        
elif sexo == "M":
    for i in grupo_a_hombres:
        if nombre.startswith(i):
            print("Hola", nombre, "perteneces al grupo A")
        else:
            print("Hola", nombre, "perteneces al grupo B")
        break
else:
    print("Favor de verificar el sexo elegido.")
