# Ejercicio 3.3
# Solicitar el nombre y la edad de una persona e indicar si es 'Mayor de edad' o 'Menor de edad'.

nombre = input("Ingrese el nombre: ").strip()

try:
    edad = int(input("Ingrese la edad (años): ").strip())
except ValueError:
    print("Edad inválida. Use un número entero.")
    exit()

if edad >= 18:
    estado = "Mayor de edad"
else:
    estado = "Menor de edad"

print(nombre + ": " + estado)
