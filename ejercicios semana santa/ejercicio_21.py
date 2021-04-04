n = int(input("ingresa un numero de 4 digitos "))
if n >= 1000 and n <=9999:
     a = int(n % 10) 
     b = int(((n-a)/10)%10)
     c = int(((n-(n % 100))/100) % 10)
     d = int(((n-(n % 1000))/1000)% 10 )
     print(f"{a}{b}{c}{d}")
else :
    print("por favor ingrsesar un numero de 4 cifras")