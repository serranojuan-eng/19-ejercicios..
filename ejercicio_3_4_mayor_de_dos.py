# Ejercicio 3.4
# Determinar el mayor de dos números enteros.

def main():
    try:
        n1 = int(input("Ingrese el primer número entero: ").strip())
        n2 = int(input("Ingrese el segundo número entero: ").strip())
    except ValueError:
        print("Entrada inválida. Use números enteros.")
        return
    if n1 > n2:
        mayor = n1
    elif n2 > n1:
        mayor = n2
    else:
        print("Los dos números son iguales:", n1)
        return
    print("El mayor es:", mayor)

if __name__ == '__main__':
    main()
