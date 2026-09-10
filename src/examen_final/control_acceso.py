"""
Control de Acceso con Intentos (Bucle while y break)
Escribe un programa que simule el acceso a una cuenta personal mediante una contraseña previamente definida (por ejemplo, "python123").
- El usuario tiene un máximo de 3 intentos para ingresar la clave correcta.
- Si ingresa la contraseña correcta, el programa debe mostrar "Acceso concedido" y terminar inmediatamente con break.
- Si se equivoca, debe mostrar cuántos intentos le quedan.
- Si agota los 3 intentos sin éxito, debe imprimir "Cuenta bloqueada por seguridad".
"""

contraseña_correcta: str = "python123"
intentos: int = 0

while intentos < 3:
    clave: str = input("Ingresa la contraseña: ")
    
    if contrasena_correcta == clave:
        print("Acceso concedido")
        break
    else:
        print("Error sigue intentando")
        intentos = intentos + 1
        print(f"Te quedan {3 - intentos} intentos")

if intentos == 3:
    print("Cuenta bloqueada por seguridad")