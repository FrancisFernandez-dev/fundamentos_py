# Autor: Francis Fernández
# Descripción: Agenda de contactos usando un diccionario. Incluye agregar, ver y eliminar.

contactos = {}

def mostrar_menu():
    print("\n=== Agenda de Contactos ===")
    print("1) Agregar contacto")
    print("2) Ver contactos")
    print("3) Eliminar contacto")
    print("4) Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado correctamente.")

    elif opcion == "2":
        if not contactos:
            print("No hay contactos registrados.")
        else:
            print("\n=== Lista de Contactos ===")
            for nombre, telefono in contactos.items():
                print(f"{nombre} → {telefono}")

    elif opcion == "3":
        nombre = input("Ingresa el nombre a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]
            print(f"Contacto '{nombre}' eliminado.")
        else:
            print("Contacto no encontrado.")

    elif opcion == "4":
        print("Saliendo de la agenda...")
        break

    else:
        print("Opción inválida.")
