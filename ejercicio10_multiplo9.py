# =============================
# EJERCICIO 10 - Primer múltiplo de 9 entre N y M (For)
# =============================
print("10) Primer múltiplo de 9 entre N y M")
N = int(input("Ingrese N: "))
M = int(input("Ingrese M: "))
encontrado = False
for i in range(N, M + 1):
    if i % 9 == 0:
        print("Primer múltiplo de 9:", i)
        encontrado = True
        break
if not encontrado:
    print("No hay múltiplos de 9 en el rango.")