
def escribe_coordenadas():
    
    valores_ascii=list([48,49,50,51,52,53,54,55,56,57])
    x = input("Introduce la coordenada X (0-9): ")
    y = input("Introduce la coordenada Y (0-9): ")
    if len(x)==1 and ord(x) in valores_ascii and len(y)==1 and ord(y) in valores_ascii:
        return [int(x),int(y)]
    elif x.lower()=="salir" or y.lower()=="salir":
        return ["salir","salir"]
    else:
        print("Entrada inválida. Introduce un número válido o salir.")

