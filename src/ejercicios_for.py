##1.crear una lista de ingredientes ["camote","papa","queso","huevo"]
#  crear un programa que recorra con for los elementos de la lista y retorne el valor y su indice del ingrediente"queso"
ingredientes:list[str] = ["camote", "papa", "queso", "huevo"]

for i in ingredientes:
 if i =="queso":
    print(f"el valor es :{i}")
    print("el indice es: {ingredientes.index(i)}")

print("---------------------------------------------------------------------------")

##2.del siguiente texto "errar es umano dijo el pato bajandose de la gallina " encontrar el error ortografico y corregir por el correcto. 

texto = "errar es umano dijo el pato bajandose de la gallina"
lista_texto = texto.split(" ")

for i in lista_texto:
    if i == "umano":
        lista_texto[lista_texto.index("umano")] = "humano"

print(" ".join(lista_texto))
## opcion 2
texto = "errar es umano dijo el pato bajandose de la gallina"
texto_corregido = texto.replace("umano", "humano")
print(texto_corregido)

