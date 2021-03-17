n1= float(input("ingresa la nota numero 1 \n"))
n2= float(input("ingresa la nota numero 2 \n"))
n3= float(input("ingresa la nota numero 3 \n"))
n4= float(input("ingresa la nota numero 4 \n"))
n_menor = n1
if n2 < n_menor :
    n_menor = n2
elif n3 < n_menor :
    n_menor=n3
elif n4 < n_menor:
    n_menor = n4
promedio = ((n1+n2+n3+n4)-n_menor)/3
print(f"su promedio es ={promedio} \n su nota menor es {n_menor}")