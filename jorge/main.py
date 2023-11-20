import clases as clases
import funciones as func
import numpy as np
import time as tm
import variables as constantes

#print(constantes.lado_1)
#func.hola()
salir = False
tablero1 = clases.tablero(10,10,"jugador")
print(type(tablero1))
tablero1.rellena("-")
print(tablero1)


# crear tablero --> 10x10
# colocar barcos --> posicion fija primero
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

# disparo usuario--> disparo(lado_1,lado_2,tablero_jugador)
# agua = False
# while agua == False
#     Agua --> cambio turno
#     Tocado
          #Cuantas posiciones quedan
               #posiciones = 0 o hundido = posiciones * barco(n)
#                 #si hundido cuenta +1 o resta -1 al total de barcos
                  #cuenta total de barcos
#        
#imprime tableros
##cambio turno
   # disparo cpu -->-> disparo(lado_1,lado_2,tablero_cpu)
   # agua = False
   # while agua == False
   #     Agua --> cambio turno
   #     Tocado
            #Cuantas posiciones quedan
                  #posiciones = 0 o hundido = posiciones * barco(n)
   #                 #si hundido cuenta +1 o resta -1 al total de barcos       
   #imprime tableros