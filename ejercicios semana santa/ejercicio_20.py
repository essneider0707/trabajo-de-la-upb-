cantidad = int(input("ingresa la cantidad de dinero que quieres desglosar (pesos colombianos): "))
denominaciones = [100000,50000,20000,10000,5000,2000,1000]
for i in denominaciones:
    if cantidad >= i:
        desglosado = cantidad // i
        print(str(desglosado) ,"billete de "+ str(i) + " mil pesos ")
        cantidad = cantidad % i