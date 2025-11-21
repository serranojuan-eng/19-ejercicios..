# =============================
# EJERCICIO 3 - Suma continua hasta ingresar 0 (While + continue/break)
# =============================
print("3) Suma continua hasta ingresar 0")
suma = 0
while True:
    n = int(input("Ingrese un número (0 para salir): "))
    if n == 0:
        break
    if n < 0:
        continue
    suma += n
print("La suma total de los positivos es:", suma)
print("\n")