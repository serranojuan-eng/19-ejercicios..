# Ejercicio 3.5
# Determinar si un número es par o impar.

try:
    n = int(input("Ingrese un número entero: ").strip())
except ValueError:
    print("Entrada inválida. Use un número entero.")
    exit()

if n % 2 == 0:
    print(n, "es par")
else:
    print(n, "es impar")
