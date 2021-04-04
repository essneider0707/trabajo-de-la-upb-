import math # importamos la libreria math
numero = float(input("ingresa un numero con parte decimal \n")) # pedimos a pantalla el numero con decimales
parte_decimal,parte_entera = math.modf(numero) # utilizamos modf para obtener la parte entera y la parte decimal 
#imprimos el valor del numero su parte entera y su parte decimal 
print(f"el numero es= {numero} \n su parte entera es= {parte_entera} \n su parte decimal es= {parte_decimal}  ")