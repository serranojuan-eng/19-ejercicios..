# =============================
# EJERCICIO 8 - Sumar serie armónica (For)
# =============================
print("8) Sumar serie armónica")
n = int(input("Ingrese n: "))
suma = 0
for i in range(1, n + 1):
    suma += 1 / i
print("Suma armónica:", suma)
print("\n")