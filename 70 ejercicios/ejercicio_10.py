count = 1
while 0 <= 3:
    i = 0
    if count == 1:
            nota1 = float(input("ingresa la nota numero 1 \n"))
            i = nota1
    if count ==2:
            nota2 =float(input("ingresa la nota numero 2 \n"))
            i = nota2
    if  count == 3:
            nota3 =float(input("ingresa la nota numero 3\n"))
            i = nota3
    if count == 4:
            break
    if i > 0 and  i <= 5:
            count = count + 1 
resultado = (nota1 + nota2 + nota3) / 3
print (f" su nota definitiva es = {resultado}")