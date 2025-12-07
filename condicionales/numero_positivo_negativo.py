# Autor: Francis Fernández
# Descripción: Determina si un número es positivo, negativo o cero.

print("=== Clasificación de Número ===")

num = float(input("Ingresa un número: "))

if num > 0:
    print("El número es POSITIVO.")
elif num < 0:
    print("El número es NEGATIVO.")
else:
    print("El número es CERO.")
