# Ejercicio 4.4
num = int(input("Ingrese un número entero positivo: "))
t = str(num)
n = len(t)
s = sum(int(x)**n for x in t)
print("ES Armstrong" if s==num else "NO es Armstrong")
