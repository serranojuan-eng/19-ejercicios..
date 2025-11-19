# Ejercicio 3.8
# Imprimir un mensaje según un carácter dado por el usuario (mayúscula o minúscula):
# 'a' -> 'Android', 'i' -> 'iOS', otro -> 'Opción inválida'

def main():
    c = input("Ingrese un carácter (a / i): ").strip()
    if not c:
        print("No se ingresó carácter.")
        return
    ch = c.lower()[0]
    if ch == 'a':
        print("Android")
    elif ch == 'i':
        print("iOS")
    else:
        print("Opción inválida")

if __name__ == '__main__':
    main()
