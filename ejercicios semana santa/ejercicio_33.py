año = int(input("por favor ingresar el año para saber si es biciesto o no "))
if año % 4 == 0  and año % 100 != 0:
    print("este es un año bisiesto")
else:
    print("esto no es un año bisiesto")
if año % 400 == 0:
    print("este año es un año bisiesto")

