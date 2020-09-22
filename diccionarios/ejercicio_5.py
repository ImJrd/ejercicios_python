#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
curso = {
    'Matemáticas':6,
    'Física':4,
    'Química':5
}
t_creditos = 0
for i , creditos in curso.items():
    print(i, "tiene", creditos, "creditos")
    t_creditos += creditos
print("Total de creditos del curso: ", t_creditos)
