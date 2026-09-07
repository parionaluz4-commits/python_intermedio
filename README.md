# control de flujo 
## condicionales
### la sentencia if 
esta sentencia al igual que en otros lenguajes de programacion en su escritura debemos añadir una `expresion de comparacion` termoinada en dos puntos `:`
```python 
temperatura:float-40.0
if temperatura >20:
    print("alta temperatura")
```
en este caso solo se ejecuta el bloque`if` si la condicion es `verdadera`, para controlar si la condicion es `falsa` debemos usar la sentencia `else`.
```python 
temp:int=20
if temp>35
  print("temperatura alta")
else:
   print("temperatura normal") 
 ```  
 podriamos tener muchas condicionales lo que se llamaria tecnicamente **condiciones anidadas**
 ```python 
 temp:int=20
 if temp < 20:
    if temp <10:
        print("nivel azul mucho frio")
    else:
        print("nivel verde normal")
 elif:
    if temp < 30:
            print ("nivel naranja")
    else:
            print("nivel rojo")
 
 ```
 python ofrece una mejora en la escritura de condiciones anidadas, para ello podemos usar la sentencia `elif`.

 ### sentencia match-case
 esta es una  nueva sentencia condicional, similar a los if anidados:
 ```python 
 vocal:str="a"
 match vocal:
    case"a"
    print("es una vocal")
    case"e"
    print("es una vocal")
    case"e"
    print("es una vocal")
    case"o"
    print("es una vocal")
    case"u"
    print("es una vocal")
    case _:
    print("es una consonante")

```
    una manera de hacer el codigo mas corto es:
```python
vocal:str=input("infrese la letra: ")
match vocal:
    case"a"|"e"|"i"|"o"|"u":
     print("es una vocal")
    case _:
     print("es una consonante")

```
    
## bucles 
### la sentencia while
es el primer mecanismo que existe en python para repetir instrucciones .
la semantica tras est sentencia es :`mientras se cumpla la condicion has algo`.
ejemplo

se puede cortar la ejecucion de un `while` haciendo el uso de `break`
```python
intentos:int=0
respuesta_correcta:str="ayacucho"
while intentos<3:
    respuesta_usuario:str=input("Capital Ayacucho: ")
    if respuesta_correcta==respuesta_usuario:
        print("respuesta correcta")
        break
    else:
        print("Error sigue intentando")
        intentos=intentos+1
    print(intentos)
```
### la sentencia for
python permite recorrer aquellos tipos de datos que sean **iterables**, algunos ejemplos de tipos de datos que permiten ser itereados son: cadenas de texto,listas,diccionarios,ficheros.
```python
nombre:str="gargamel" #string,texto,cadena de texto
amigos:list[str]=['pepe','lucho','juan'] #lista de texto
alumno:dic[str:int|str]={
    "dni":75445465,
    "nombre":"juancito"
}#diccionario
```
a continuacion plantearemos un ejemplo en el que vamos a recorrer una cadena de texto:
```python
for letra in texto:
    print(letra)
```
la clave para entender el ejercicio es darce cuenta que el bucle va tomando en cada iteracion, cada uno de los elementos de la variable, en el ejemplo `letra` va tomando cada una de las letras  que tiene `texto`
la variable `letra`puede tomar cualquier nombre 
**romper un bucle for**
al igual que `while` para romper o terminar un bucle un bucle `for` debemos usar `break`
*ojo* - para realizar la rotura se debe previamente cumplir una condicional.
## crear un programa que recorra un texto  y que termine la ejecucion cuando encuentre la letra a 
```python
texto:str="hola de donde eres y a donde vas"
for l in texto:
    if l =="a":
        break
else:
     print(l)
```
### Secuencias de números

Es muy habitual hacer uso de secuencias en bucles. Python aporta una función
para realizar la secuencia de números: `range()`. Esta función devuelve un
flujo de números en el rango especificado.

Su estructura es la siguiente:
La función `range(start, stop, step)` puede recibir hasta tres parámetros
posicionales:

- `start` - es *opcional* y tiene valor por defecto `0`.
- `stop` - es *obligatorio*. Este valor siempre llega hasta 1 menos que el valor
  asignado.
- `step` - es *opcional* y tiene valor por defecto `1`. Es el valor que irá
  incrementando.
## 1. Mostrar los números del 0 al 5 con la función range
```python
for numero in range(6):
    print(numero)
print("------------------------------")
```

## 2. Mostrar los números del 2 al 6
```python
for numero in range(2, 7):
    print(numero)
print("------------------------------")
```
## 3. mostrar los numeros pares que existen entre 1 y 10 
```python
for pares in range(2,11,2):
    print(pares)
```    
> [!TIP] Se suele utilizar nombres de variables `i,j,k` paara 
lo que se denomina 'contadores'. o la variable que va despues
del `for`.