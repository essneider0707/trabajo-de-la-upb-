numero =float(input("ingresa el numero para saber si es negativo o positivo \n"))
if numero < 0 and numero % 2 == 0 :
    print(numero,"este numero es negativo par")
elif numero < 0 and numero % 2 != 0 :
    print(numero,"este numero es negativo impar")
elif numero > 0 and numero % 2 == 0 :
    print(numero,"este numero es positivo par")
elif numero > 0 and numero % 2 != 0 :
    print(numero,"este numero es positivo impar")
print("fin")