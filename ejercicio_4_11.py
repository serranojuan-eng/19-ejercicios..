# Ejercicio 4.11
n=int(input("Ingrese un número: "))
if n<0: print("No existe factorial negativo")
else:
    f=1
    for x in range(1,n+1): f*=x
    print("Factorial:",f)
