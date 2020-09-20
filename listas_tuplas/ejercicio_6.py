#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nota_m = input("Calificación obtenida en " + asignaturas[0] + " ")
nota_f = input("Calificación obtenida en " + asignaturas[1] + " ")
nota_q = input("Calificación obtenida en " + asignaturas[2] + " ")
nota_h = input("Calificación obtenida en " + asignaturas[3] + " ")
nota_l = input("Calificación obtenida en " + asignaturas[4] + " ")

if float(nota_m) > 7:
    asignaturas.remove("Matemáticas")
if float(nota_f) > 7:
    asignaturas.remove("Física")
if float(nota_q) > 7:
    asignaturas.remove("Química")
if float(nota_h) > 7:
    asignaturas.remove("Historia")
if float(nota_l) > 7:
    asignaturas.remove("Lengua")
if len(asignaturas) == 0:
    print("Aprobo todas las asignaturas")
else:
    for i in asignaturas:
        print("Debe cursar las materias " + str(asignaturas))
        break
    
    
