# Ejercicio 3.3
# Solicitar el nombre y la edad de una persona e indicar si es 'Mayor de edad' o 'Menor de edad'.

def main():
    nombre = input("Ingrese el nombre: ").strip()
    try:
        edad = int(input("Ingrese la edad (años): ").strip())
    except ValueError:
        print("Edad inválida. Use un número entero.")
        return
    estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
    print(f"{nombre}: {estado}")

if __name__ == '__main__':
    main()
