# Ejercicio 3.13
# Conocer el valor del descuento de un artículo según su tipo:
# Tipo 1 -> 12.5%
# Tipo 2 -> 8.3%
# Tipo 3 -> 3.2%
# Otro   -> 0.0%

def main():
    try:
        precio = float(input("Ingrese el precio del artículo: ").strip())
    except ValueError:
        print("Precio inválido.")
        return
    tipo = input("Ingrese el tipo (1/2/3/otro): ").strip().lower()
    if tipo == '1' or tipo == '1 ':
        descuento = 0.125
    elif tipo == '2':
        descuento = 0.083
    elif tipo == '3':
        descuento = 0.032
    else:
        descuento = 0.0
    valor_desc = precio * descuento
    precio_final = precio - valor_desc
    print(f"Descuento aplicado: {descuento*100:.2f}% -> Valor descuento: {valor_desc:.2f}")
    print(f"Precio final: {precio_final:.2f}")

if __name__ == '__main__':
    main()
