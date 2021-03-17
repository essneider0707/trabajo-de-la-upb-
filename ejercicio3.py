p1 = 0.15
p2 = 0.15
p3 = 0.20
p4 = 0.20
p5 = 0.30
count = 1
while count <= 5:
    i = 0
    try:
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
        if i > 0 and  i <= 5:
            count = count + 1 
    except:
        print("este valor no es valido")
resultado = (nota1*p1) +( nota2*p2) +( nota3*p3) + (nota4*p4) +(nota5*p5)
print (f" su nota definitiva es ={resultado}")
if resultado >= 3:
        print("aprobo la materia con =",resultado)
else :
        print("reprobado su nota es =" , resultado) 


