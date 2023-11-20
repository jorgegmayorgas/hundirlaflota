#### funcion para resetear, respetando el orden de los barcos

def arregla_barcos(tablero):
    tablero[tablero == "X"] = "O"

## otra forma
def arregla_barcos(tablero):
    tablero = np.where(tablero == "X", "O", tablero)
    
    
    

ef genera_barco(tablero, tam_barco = 4):
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    orientaciones =["N","S","O","E"]

    while True:
        orientacion = orientaciones[random.randint(0,3)]
        orientacion = random.choice(["N","S","O","E"])
        origen = (random.randint(0,num_filas -1), random.randint(0,num_columnas -1))
        print("voy a usar origen", origen)
        fila = origen[0]
        columna = origen[1]
        barco = []
        if tablero[origen] != "O" and tablero[origen] != "X": 
            barco.append(origen)
            for i in range(tam_barco - 1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "E":
                    columna += 1
                else:
                    columna -= 1
                if fila >= num_filas or fila < 0:
                    print("Me salgo del tablero")
                    break
                elif columna >= num_columnas or columna < 0:
                    print("Me salgo del tablero")
                    break
                elif tablero[fila, columna] == "X":
                    break
                barco.append((fila,columna))

            if len(barco) != tam_barco:
                continue
            else:
                coloca_barco(tablero, barco)
                break
        else:
            continue