
vocal:str=input("infrese la letra: ")
match vocal:
    case"a"|"e"|"i"|"o"|"u"
     print("es una vocal")
    case _:
     print("es una consonante")
