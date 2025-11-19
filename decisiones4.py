notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota del trabajo {i+1}: "))
    notas.append(nota)
promedio = sum(notas) / 5
if promedio > 3.5:
    print("El estudiante ganó el curso.")
else:
    print("El estudiante perdió el curso.")
