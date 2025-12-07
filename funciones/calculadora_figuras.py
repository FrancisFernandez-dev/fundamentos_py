# Autor: Francis Fernández
# Descripción: Calculadora de áreas usando funciones modulares.

def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return 3.14159 * (radio ** 2)

def menu():
    print("=== Calculadora de Figuras Geométricas ===")
    print("1) Área de cuadrado")
    print("2) Área de rectángulo")
    print("3) Área de círculo")
    print("4) Salir")

while True:
    menu()
    opcion = input("Selecciona opción: ")

    if opcion == "1":
        lado = float(input("Lado del cuadrado: "))
        print("Área:", area_cuadrado(lado))

    elif opcion == "2":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("Área:", area_rectangulo(base, altura))

    elif opcion == "3":
        radio = float(input("Radio del círculo: "))
        print("Área:", area_circulo(radio))

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
