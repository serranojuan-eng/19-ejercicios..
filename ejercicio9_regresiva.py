# =============================
# EJERCICIO 9 - Cuenta regresiva con alerta (For)
# =============================
print("9) Cuenta regresiva con alerta")
n = int(input("Ingrese número para cuenta regresiva: "))
for i in range(n, -1, -1):
    if i % 7 == 0 and i != 0:
        print(i, "→ Alerta: múltiplo de 7")
    else:
        print(i)
print("Fin de la cuenta regresiva")
print("\n")