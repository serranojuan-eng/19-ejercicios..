# Ejercicio 4.3
num = int(input("Ingrese un número entero positivo: "))
if num > 0:
    t = str(num)
    print("Cifras:", len(t))
    print("Suma:", sum(int(x) for x in t))
else:
    print("El número no es positivo")
