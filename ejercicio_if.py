"""1. escriba un programa que acepte 1 opcion de dos jugadores en piedra_papel
- entrada:persona 1= piedra, persona2=papel,
- salida: gana persona2, papel envuelve piedra

2. escribe un programa que acepte 3 numeros y calcule el minimo 
- entradab : 7,4,8
- salida : 4 
"""
p1 = input("Persona 1: ")
p2 = input("Persona 2: ")

if p1 == p2:
    print("Empate")
else:
    if p1 == "piedra":
        if p2 == "papel":
            print("gana persona1, papel envuelve piedra")
        else:
            print("gana persona2,papel envuelve piedra")
    
    if p1 == "papel":
        if p2 == "piedra":
            print("gana persona1,papel envuelve piedra")
        else:
            print("gana persona2,papel envuelve piedra")
    


###
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 < num2:
    if num1 < num3:
        print("El mínimo es:", num1)
    else:
        print("El mínimo es:", num3)
else:
    if num2 < num3:
        print("El mínimo es:", num2)
    else:
        print("El mínimo es:", num3)