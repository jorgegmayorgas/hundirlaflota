
class tablero:
    #Atributos y métodos, las cosas de la clase
    def __init__(self, longitud_lado_1=10 , longitud_lado_2=10):
        self.longitud_lado_1 = longitud_lado_1
        self.longitud_lado_2= longitud_lado_2
        #self.posiciones = posiciones

    def muestra (self):
        print(self)
class barco:
     #posiciones = 4

    def __init__(self, coordenada_x=0 , coordenada_y=0, posiciones = 4,caracter="0"):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.posiciones = posiciones
        self.caracter = caracter


    
