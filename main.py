## USANDO WHILE CEAR UN PROGRAMA QUE ME DE UNA PREGUNTA para responder y que solo tenga 3 oportunidades para dar con la respuesta correcta
respuesta_correcta = "Python"
intentos = 0
respuesta = ""
continuar = "S"

while continuar == "S" and intentos < 3:
    respuesta = input("¿Cuál es el lenguaje de programación que estamos utilizando? ")
    intentos += 1

    if respuesta == respuesta_correcta:
        print("Respuesta correcta")
        continuar = "N"
    else:
        print("Respuesta incorrecta")

        if intentos < 3:
            continuar = input("¿Desea intentar nuevamente? (S/N): ")
        else:
            continuar = "N"

print("Programa terminado")

