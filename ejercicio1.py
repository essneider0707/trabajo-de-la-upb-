total = 0
contar = 0
print ("Introduzca un valor numerico  (0 para salir): ")
dato = int(input())
while dato != 0:
    total =  total + dato
    contar = contar + 1
    print ("Introduzca un valor numerico (0 para salir): ")
    dato = int(input())
promedio = int(total / contar)
print ("Promedio de la suma de los valores es: " + str(promedio))
print ("cantidad de datos ingresados",contar)
print(" el valor de la suma es =",total)