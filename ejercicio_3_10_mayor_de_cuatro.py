# Ejercicio 3.10
# Determinar el mayor entre cuatro posibles números.

def main():
    try:
        nums = [float(input(f"Ingrese el número {i+1}: ").strip()) for i in range(4)]
    except ValueError:
        print("Entrada inválida, use números.")
        return
    mayor = max(nums)
    print("Los números ingresados son:", nums)
    print("El mayor es:", mayor)

if __name__ == '__main__':
    main()
