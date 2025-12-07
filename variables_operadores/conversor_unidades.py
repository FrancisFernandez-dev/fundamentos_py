# Autor: Francis Fernández
# Descripción: Conversor de unidades utilizando variables, operadores y entrada del usuario.

print("=== Conversor de Unidades Básico ===")

print("1) Celsius a Fahrenheit")
print("2) Kilómetros a Millas")
print("3) Pesos chilenos a Dólares")
opcion = int(input("Selecciona una opción (1-3): "))

if opcion == 1:
    celsius = float(input("Ingresa grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")

elif opcion == 2:
    km = float(input("Ingresa kilómetros: "))
    millas = km * 0.621371
    print(f"{km} km equivalen a {millas} millas")

elif opcion == 3:
    pesos = float(input("Ingresa pesos chilenos: "))
    dolar = pesos / 950  # Valor ejemplo
    print(f"${pesos} CLP equivalen a {dolar} USD")

else:
    print("Opción no válida.")
