costo = float(input("Ingrese el costo del artículo: "))
if costo > 150000:
    descuento = costo * 0.05
else:
    descuento = 0
print("El valor del descuento es:", descuento)
