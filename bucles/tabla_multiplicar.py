# Autor: Francis Fernández
# Descripción: Generador de tabla de multiplicar usando un bucle FOR.

print("=== Tabla de Multiplicar ===")
n = int(input("Ingresa un número: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
