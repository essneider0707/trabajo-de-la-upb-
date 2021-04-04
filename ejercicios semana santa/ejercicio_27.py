p1 = 0.15
p2 = 0.15
p3 = 0.20
p4 = 0.20
p5 = 0.30
count = 1
while True:
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
    if i > 0 and  i <= 5:
            count = count + 1 
    elif count == 6:
            break
resultado = (nota1*p1) +( nota2*p2) +( nota3*p3) + (nota4*p4) +(nota5*p5)
if resultado < 3:
    print("su no es =",resultado,"hey parcero ponte las pilas que reprobaste")
elif resultado >= 3:
    print("su no es =",resultado,"hey parcero la buena aprovaste , pero tienes que sacar mejor nota la proxima ")
elif resultado >= 4.5:
    print("su no es =",resultado,"hey parcero que teso ,sigue asi felicitaciones ")