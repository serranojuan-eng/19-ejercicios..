x = float(input("Ingrese un número: "))
print("Ingrese los tres intervalos abiertos (mínimo y máximo para cada uno):")

a1 = float(input("Mínimo intervalo 1: "))
b1 = float(input("Máximo intervalo 1: "))

a2 = float(input("Mínimo intervalo 2: "))
b2 = float(input("Máximo intervalo 2: "))

a3 = float(input("Mínimo intervalo 3: "))
b3 = float(input("Máximo intervalo 3: "))

if (a1 < x < b1) or (a2 < x < b2) or (a3 < x < b3):
    print("El número está dentro de alguno de los intervalos.")
else:
    print("El número está fuera de todos los intervalos.")
