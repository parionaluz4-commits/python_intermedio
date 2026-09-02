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