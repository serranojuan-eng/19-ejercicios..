# Ejercicio 3.8
# Imprimir un mensaje según un carácter dado por el usuario (mayúscula o minúscula):
# 'a' -> 'Android', 'i' -> 'iOS', otro -> 'Opción inválida'

c = input("Ingrese un carácter (a / i): ").strip()

if not c:
    print("No se ingresó carácter.")
    exit()

ch = c.lower()[0]

if ch == 'a':
    print("Android")
elif ch == 'i':
    print("iOS")
else:
    print("Opción inválida")

