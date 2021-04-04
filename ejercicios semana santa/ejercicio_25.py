precio = float(input("ingresa el valor del producto "))
iva = precio  * 0.19
descuento = precio * 0.05
if precio <= 150.000:
    precio = precio + iva 
    print(precio,"este es el valor a pagar por todo")
elif precio > 150.000 :
    precio = precio + iva 
    total = precio - descuento
    print(f"{total} este es el precio a pagar con el descuento del 5% por compras mayores a 150.000 y este es el valor del decuento del producto  {descuento}")