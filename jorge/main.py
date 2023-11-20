import clases as clases
import funciones as func
import numpy as np
import time as tm
import variables as constantes

#print(constantes.lado_1)
#func.hola()
salir = False
# crear tablero --> 10x10
# colocar barcos --> fija primero
#     hay que tener en cuenta los limites del tablero
#     no se pueden solapar barcos
while salir == False:
     lado_1=input("Diga primera coordenada o salir:")
     if lado_1.lower() == "salir":
        salir=True
        continue
     else:
        lado_2=input("Diga segunda coordenada o salir:")
        if lado_2.lower() == "salir":
           salir=True
     #tm.sleep(5)
     #disparo(lado1,lado2)
     #turno cpu
     #semilla aleatoria
     #disparo(lado1,lado2)


# nombre usuario

# disparo -->
# agua = False
# while agua == False
#     Agua --> cambio turno
#     Tocado
          #Cuantas posiciones quedan
               #posiciones = 0 o hundido = posiciones * barco(n)
#     