# =============================
# EJERCICIO 4 - Menú repetitivo (While)
# =============================
print("4) Menú repetitivo de operaciones")
while True:
    print("\n1. Sumar\n2. Restar\n3. Salir")
    opcion = input("Seleccione opción: ")
    if opcion == "3":
        print("Fin del programa.")
        break
    if opcion in ("1", "2"):
        x = float(input("Primer número: "))
        y = float(input("Segundo número: "))
        if opcion == "1":
            print("Resultado:", x + y)
        else:
            print("Resultado:", x - y)
    else:
        print("Opción inválida.")
print("\n")