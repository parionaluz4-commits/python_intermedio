""" 
Clasificador de Clima (Condicionales if-elif-else)
Escribe un programa que pida al usuario la temperatura actual en grados Celsius (número decimal) y
  muestre un mensaje según los siguientes rangos:
- Si es menor a 10: "Mucho frío"
- Si está entre 10 y 25 (inclusive): "Clima templado"
- Si está entre 26 y 35 (inclusive): "Clima cálido"
- Si es mayor a 35: "Alerta de calor extremo"
 Clasificador de Clima
 Pide la temperatura al usuario
"""
temperatura: float = float(input("Ingresa la temperatura actual en °C: "))

if temperatura < 10:
    print("Mucho frío")
elif 10 <= temperatura <= 25:
    print("Clima templado")
elif 26 <= temperatura <= 35: 
    print("Clima cálido")
else:
    print("Alerta de calor extremo")
