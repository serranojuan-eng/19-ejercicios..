x = int(input("Ingrese un número entero: "))
minimo = int(input("Ingrese el valor mínimo del intervalo: "))
maximo = int(input("Ingrese el valor máximo del intervalo: "))

if minimo <= x <= maximo:
    print("El número está dentro del intervalo cerrado.")
else:
    print("El número está fuera del intervalo.")
