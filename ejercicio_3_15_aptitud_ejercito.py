# Ejercicio 3.15
# Verificar si un aspirante es apto para ingresar al ejército según:
# - Si es mujer: estatura > 1.60 m y edad entre 20 y 25 años
# - Si es hombre: estatura > 1.65 m y edad entre 18 y 24 años
# - Tanto mujeres como hombres deben ser solteros.

def main():
    sexo = input("Ingrese sexo (M para mujer, H para hombre): ").strip().upper()
    try:
        estatura = float(input("Ingrese estatura en metros (ej. 1.70): ").strip())
        edad = int(input("Ingrese edad en años: ").strip())
    except ValueError:
        print("Entrada inválida para estatura o edad.")
        return
    estado_civil = input("Ingrese estado civil (soltero/otro): ").strip().lower()
    apto = False
    if estado_civil != 'soltero' and estado_civil != 'soltera':
        print("No es apto: debe ser soltero/a.")
        return
    if sexo == 'M':
        if estatura > 1.60 and 20 <= edad <= 25:
            apto = True
    elif sexo == 'H':
        if estatura > 1.65 and 18 <= edad <= 24:
            apto = True
    else:
        print("Sexo no reconocido. Use M o H.")
        return
    if apto:
        print("El aspirante es APT0 para ingresar al ejército.")
    else:
        print("El aspirante NO es apto para ingresar al ejército.")

if __name__ == '__main__':
    main()
