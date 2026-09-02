## crear un programa de login que mientras que la persona no ponga el usuario y contraseña correcto le siga pidiendo esa informacion si el usuario/contraseña son correctos entonces darle un mensaje de bienvenida y salir del programa 
usuario_correcto:str = "admin"
contrasena_correcta:str = "1234"
intentos:int = 0

while intentos < 3:
    usuario:str = input("Usuario: ")
    contrasena:str = input("Contraseña: ")
    
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("Bienvenido al sistema")
        break
    else:
        print("Error, sigue intentando")
        intentos = intentos + 1
        print("Te quedan", 3 - intentos, "intentos")

if intentos == 3:
    print("Cuenta bloqueada")