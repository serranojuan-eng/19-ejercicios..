# Ejercicio 3.7
# Determinar si un número real x se encuentra dentro de alguno de los siguientes rangos:
# (3.5, 7.8] o [9.3, 45.3]  (si la imagen era distinta, ajuste los límites según su enunciado).

def main():
    try:
        x = float(input("Ingrese un número real x: ").strip())
    except ValueError:
        print("Entrada inválida. Use un número real.")
        return
    in_first = x > 3.5 and x <= 7.8
    in_second = x >= 9.3 and x <= 45.3
    if in_first or in_second:
        print(f"{x} está en alguno de los rangos especificados")
    else:
        print(f"{x} NO está en ninguno de los rangos especificados")

if __name__ == '__main__':
    main()
