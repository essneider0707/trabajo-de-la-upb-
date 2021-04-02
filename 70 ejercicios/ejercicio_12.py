import math 
gravedad = 9.8
altura = float(input("ingresa la altura desde la cual el objeto es lanzado ( en metros )\n"))
tiempo = math.sqrt ((2*altura)/gravedad)
print (" el tiempo que se demora caer el objeto es =",tiempo,"segundos")