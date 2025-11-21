# Ejercicio 4.24
t=int(input("Tabla a repasar (1-20): "))
a=0
for i in range(1,11):
    r=int(input(f"{t} x {i} = "))
    if r==t*i:
        print("Correcto"); a+=1
    else:
        print("Incorrecto. Era:",t*i)
print("Aciertos:",a)
if a<=5: print("Insuficiente")
elif a<=7: print("Aceptable")
elif a<=9: print("Sobresaliente")
else: print("Excelente")
