def pidenumero():
    lista=[]
    while True :
        n =int(input("ingresa el valor numerico(0 para terminar)\n"))
        if n == 0:
            break
        else:
            lista.append(n)
    return lista


def mayorMenor(lista):
    mayor = 0
    menor = 99999999
    for numero in lista :
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    return mayor,menor


lista =pidenumero()
mayor,menor = mayorMenor(lista)
print(f"mayor\n{mayor}\nmenor\n{menor}")  

            
        
    


    


  



