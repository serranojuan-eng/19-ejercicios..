# Ejercicio 4.10
c = int(input("Cantidad de estudiantes: "))
a=i=0
for _ in range(c):
    codigo=input("Código: ")
    e=input("Plataforma (android/ios): ").lower()
    if e=="android": a+=1
    elif e=="ios": i+=1
print("Android:",a,"iOS:",i)
print("Ganador:", "android" if a>i else "ios" if i>a else "Empate")
