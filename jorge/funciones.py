def escribe_coordenadas():
    try:
            x = int(input("Introduce la coordenada X (0-9): "))
            y = int(input("Introduce la coordenada Y (0-9): "))
            if 0 <= x <= 9 and 0 <= y <= 9:#comprobación valores dentro del rango
                return [x,y]
            else:
                print("Coordenadas fuera de rango. Introduce coordenadas entre 0 y 9.")
    except ValueError:
            if x.lower() =="salir" or y.lower()=="salir":
                return False
            else:
                print("Entrada inválida. Introduce un número válido.")
