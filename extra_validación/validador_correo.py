# Autor: Francis Fernández
# Descripción: Validador simple de correo usando operaciones con strings.

correo = input("Ingresa tu correo: ")

if "@" in correo and "." in correo:
    print("Correo válido.")
else:
    print("Correo inválido.")
