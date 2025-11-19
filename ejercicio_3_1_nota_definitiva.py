# Ejercicio 3.1
# Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0.
# Debe imprimir el valor ingresado, y si la nota es mayor o igual a 4.0,
# deberá imprimir un mensaje de felicitaciones.

def main():
    try:
        nota = float(input("Ingrese la nota definitiva (0.0 - 5.0): ").strip())
    except ValueError:
        print("Entrada inválida. Use un número decimal como 3.7")
        return
    if nota < 0 or nota > 5:
        print("La nota debe estar entre 0.0 y 5.0")
        return
    print(f"Nota ingresada: {nota:.2f}")
    if nota >= 4.0:
        print("¡Felicitaciones! Obtuvo una buena nota.")

if __name__ == '__main__':
    main()
