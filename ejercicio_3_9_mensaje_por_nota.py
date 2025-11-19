# Ejercicio 3.9
# Imprimir un mensaje según la nota definitiva entre 0.0 y 5.0:
# < 3.0 -> 'Insuficiente'
# <= 3.5 -> 'Aceptable'
# <= 4.0 -> 'Sobresaliente'
# <= 5.0 -> 'Excelente'

def main():
    try:
        nota = float(input("Ingrese la nota (0.0 - 5.0): ").strip())
    except ValueError:
        print("Entrada inválida.")
        return
    if nota < 0 or nota > 5:
        print("La nota debe estar entre 0.0 y 5.0")
        return
    if nota < 3.0:
        msg = "Insuficiente"
    elif nota <= 3.5:
        msg = "Aceptable"
    elif nota <= 4.0:
        msg = "Sobresaliente"
    else:
        msg = "Excelente"
    print(f"Nota: {nota:.2f} -> {msg}")

if __name__ == '__main__':
    main()
