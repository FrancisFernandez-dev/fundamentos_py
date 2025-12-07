# Autor: Francis Fernández
# Descripción: Script que solicita datos del usuario utilizando diferentes tipos: str, int, float, bool.

print("=== Formulario de Registro ===")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura en metros: "))
estudiante = input("¿Eres estudiante? (sí/no): ")

es_estudiante = estudiante.lower() == "sí"

print("\n=== Resumen de Datos Ingresados ===")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Estatura: {estatura} m")
print(f"¿Es estudiante?: {es_estudiante}")
