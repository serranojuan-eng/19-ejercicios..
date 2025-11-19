# Ejercicio 3.12
# Reescribir el Ejemplo 3.8 pero con decisiones múltiples (versión alternativa).
# Aquí pediremos una opción numérica y usaremos varias ramas.

def main():
    print("Seleccione una opción:")
    print("1 - Android\n2 - iOS\n3 - Otro")
    opcion = input("Ingrese la opción (1/2/3): ").strip()
    if opcion == '1':
        print("Android")
    elif opcion == '2':
        print("iOS")
    elif opcion == '3':
        print("Opción: Otro sistema")
    else:
        print("Opción inválida")

if __name__ == '__main__':
    main()
