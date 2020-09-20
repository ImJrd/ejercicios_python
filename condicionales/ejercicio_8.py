#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#Inaceptable 0.0, Aceptable 0.4, Meritorio 0.6 o mas
puntuacion = input("Ingrese su puntuación: ")
dinero = 2400
if float(puntuacion) == 0:
    print("Su nivel de rendimiento es inaceptable\nSu pago es de $" + str(dinero))
if float(puntuacion) == 0.4:
    print("Su nivel de rendimiento es aceptable\nSu pago es de $", (dinero+(dinero*float(puntuacion))))
if float(puntuacion) >=0.6:
    print("Su nivel de rendimiento es meritorio\nSu pago es de $",(dinero+(dinero*float(puntuacion))))
