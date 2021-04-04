#definimos p1 p2 p3 p4 p5 como constantes que equivalen al porcentaje de cada nota 
p1 = 0.15
p2 = 0.15
p3 = 0.20
p4 = 0.20
p5 = 0.30
# definimos un contador
count = 1
# iniciamos un ciclo while que se ejecuta 5 veces 
while 0 <= 5:
    i = 0
    if count == 1:
            nota1 = float(input("ingresa la nota numero 1 \n"))
            i = nota1
    elif count ==2:
            nota2 =float(input("ingresa la nota numero 2 \n"))
            i = nota2
    elif count == 3:
            nota3 =float(input("ingresa la nota numero 3\n"))
            i = nota3
    elif count == 4:
            nota4 =float(input("ingresa la nota numero 4\n"))
            i = nota4
    elif count == 5:
            nota5 =float(input("ingresa la nota numero 5\n"))
            i = nota5
#se define esta condicional para que la nota no pase de 5 y tampoco se menor a 0
    if i > 0 and  i <= 5:
            count = count + 1 
    if count == 6:
            break
#se realiza el proceso de multiplicar cada nota con su porcentaje y sumarlos 
resultado = (nota1*p1) +( nota2*p2) +( nota3*p3) + (nota4*p4) +(nota5*p5)
print (f" su nota definitiva es ={resultado}")