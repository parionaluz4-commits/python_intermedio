"""
 Contador de Vocales en un Texto (Bucle for y range)
Pide al usuario que ingrese una frase o palabra. Utilizando un bucle for, recorre la cadena e
 imprime únicamente los números pares correspondiente a las posiciones/índices de los caracteres, junto con el carácter en dicha posición.
Pista: Puedes combinar la función range() junto con len(texto) para iterar sobre los índices de la cadena.
"""
texto: str = input("hola de donde eres y a donde va: ")

for i in range(0, len(texto), 2): 
    print("Indice", i, ":", texto[i])