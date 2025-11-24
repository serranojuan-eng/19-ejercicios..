#ejercicio3.1
try:
    nota = float(input("Ingrese la nota definitiva (0.0 - 5.0): ").strip())
except ValueError:
    print("Entrada inválida. Use un número decimal como 3.7")
    exit()

if nota < 0 or nota > 5:
    print("La nota debe estar entre 0.0 y 5.0")
    exit()

print("Nota ingresada:", nota)

if nota >= 4.0:
    print("¡Felicitaciones! Obtuvo una buena nota.")


