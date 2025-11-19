a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = b**2 - 4*a*c

if a != 0 and discriminante >= 0:
    print("La ecuación cuadrática tiene solución.")
else:
    print("La ecuación cuadrática no tiene solución.")
