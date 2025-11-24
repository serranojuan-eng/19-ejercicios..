# Ejercicio 3.6
# Determinar si un número real x se encuentra dentro del rango (3.5, 7.8]

try:
    x = float(input("Ingrese un número real x: ").strip())
except ValueError:
    print("Entrada inválida. Use un número real.")
    exit()

# Rango (3.5, 7.8] => x > 3.5 y x <= 7.8
if x > 3.5 and x <= 7.8:
    print(x, "está en el rango (3.5, 7.8]")
else:
    print(x, "NO está en el rango (3.5, 7.8]")

