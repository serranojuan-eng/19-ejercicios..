numero = int(input("Ingrese un número entero entre 0 y 20: "))
if numero < 2:
    print("No es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es un número primo.")
    else:
        print("No es un número primo.")
