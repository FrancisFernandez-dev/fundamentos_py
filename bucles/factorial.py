# Autor: Francis Fernández
# Descripción: Calculadora de factorial usando un bucle WHILE.

print("=== Cálculo de Factorial ===")

n = int(input("Ingresa un número entero: "))
resultado = 1
contador = 1

while contador <= n:
    resultado *= contador
    contador += 1

print(f"El factorial de {n} es: {resultado}")
