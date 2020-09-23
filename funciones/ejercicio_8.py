#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
def square(example):
    list = []
    for i in example:
        list.append(i**2)
    return list

def list_statistics(example):
    statis = {}
    statis["media"] = sum(example)/len(example)
    statis["varianza"] = sum(square(example))/len(example)-statis["media"]**2
    statis["desviacion tipica"] = statis["varianza"]**0.5
    return statis


print(list_statistics([1, 2, 3, 4, 5]))
