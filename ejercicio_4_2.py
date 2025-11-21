# Ejercicio 4.2
cantidad = int(input("Ingrese la cantidad de estudiantes: "))
ap = rp = 0
s = 0
for i in range(cantidad):
    codigo = input("Código del estudiante: ")
    nota = float(input("Nota definitiva: "))
    s += nota
    if nota >= 3: ap += 1
    else: rp += 1
print("Aprobados:", ap)
print("Reprobados:", rp)
print("Promedio:", s/cantidad)
