def hola():
    print("Hola")

def disparo(valor,tablero):
    if valor.upper() == "O":
        valor = "X"
        #print(valor)
        print("Acierto") #definir tocado hundido
        return valor
    else:
        print("Agua")
        valor = "-"
        return valor

def tocado_hundido(tablero):
    mensaje=""
    for indice,elemento in enumerate(tablero):
        pass        
    return mensaje

def barco(tablero,tamanyo):
    fila_inicial = 0
    columna_inicial = 0
    tupla_limite_superior = tablero.shape
    limite_ejex = tupla_limite_superior[0]
    limite_ejey = tupla_limite_superior[1]
    #print(limite_ejex,limite_ejey)
    ejex = rd.randrange(limite_ejex-1)
    ejey = rd.randrange(limite_ejey-1)
    print(ejex,":",ejey)

def impacto (self,coordenada_x=0, coordenada_y=0,posiciones):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.posiciones = posiciones