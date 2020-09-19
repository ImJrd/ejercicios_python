#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nota_m = input("Calificación obtenida en " + asignaturas[0] + " ")
nota_f = input("Calificación obtenida en " + asignaturas[1 + " "])
nota_q = input("Calificación obtenida en " + asignaturas[2] + " ")
nota_h = input("Calificación obtenida en " + asignaturas[3] + " ")
nota_l = input("Calificación obtenida en " + asignaturas[4] + " ")
print("En " + asignaturas[0] + " has sacado " + nota_m)
print("En " + asignaturas[1] + " has sacado " + nota_f)
print("En " + asignaturas[2] + " has sacado " + nota_q)
print("En " + asignaturas[3] + " has sacado " + nota_h)
print("En " + asignaturas[4] + " has sacado " + nota_l)
