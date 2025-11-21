# =============================
# EJERCICIO 1 - Serie Fibonacci hasta N (While)
# =============================
print("\n1) Serie Fibonacci hasta N")
N = int(input("Ingrese un número N: "))
a, b = 0, 1
while a <= N:
    print(a, end=" ")
    a, b = b, a + b
print("\n")