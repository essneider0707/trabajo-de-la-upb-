mayor = 0
menor = 0
a = 0 
cond = True
i = 1
while cond:
    a =int(input("ingresa un valor numerico(0 para salir)\n"))
    if a != 0:
        if a > 0:
            if a > mayor:
                mayor = a
            if a < menor or  i==1:
                menor = a 
            i = i+1
    else:
        print(f"el numero mayor es {mayor} \n el numero menor es {menor}")
        cond = False        

                   