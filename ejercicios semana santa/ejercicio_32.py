print("por viajar mas de 1000 km y mas de 7 dias obtienes un descuento del 15%")
distancia = float (input("por favor ingresar la cantidad de km a viajar ")) 
dias = int(input("por favor ingresar la cantidad de dias que viajara "))
precio = distancia * 5000
descuento = precio * 0.15
if distancia > 1000 and dias > 7 :
    print("oh eres un viajero increible has obtenido un descuento del 15%")
    precio = precio - descuento 
    print(precio)
if precio < 100000 or distancia < 20:
    print("lo sentimos la cantidad minima para poder realizar el vuelo es de 20 km a recorrer") 
else:
    print("el costo por realizar tu viaje es ",precio)
