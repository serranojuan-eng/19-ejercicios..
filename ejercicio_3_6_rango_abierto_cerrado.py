# Ejercicio 3.6
# Determinar si un número real x se encuentra dentro del rango (3.5, 7.8]

def main():
    try:
        x = float(input("Ingrese un número real x: ").strip())
    except ValueError:
        print("Entrada inválida. Use un número real.")
        return
    # Rango (3.5, 7.8] => x > 3.5 and x <= 7.8
    if x > 3.5 and x <= 7.8:
        print(f"{x} está en el rango (3.5, 7.8]")
    else:
        print(f"{x} NO está en el rango (3.5, 7.8]")

if __name__ == '__main__':
    main()
