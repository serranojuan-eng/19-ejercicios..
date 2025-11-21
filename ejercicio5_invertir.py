# =============================
# EJERCICIO 5 - Invertir un número entero (While)
# =============================
print("5) Invertir un número entero")
n = int(input("Ingrese un número entero: "))
invertido = 0
while n > 0:
    dig = n % 10
    invertido = invertido * 10 + dig
    n //= 10
print("Número invertido:", invertido)
print("\n")