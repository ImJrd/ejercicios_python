#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math

def circle_area(radius):
    area = math.pi*(radius**2)
    return area

def cilinder_volume(radius, high):
    return circle_area(radius)*high
    

print(cilinder_volume(8, 15))
