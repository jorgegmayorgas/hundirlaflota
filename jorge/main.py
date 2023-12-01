from clases import Tablero
from datetime import datetime
import variables as variables
import funciones as func
import numpy as np
import pandas as pd
from playsound import playsound
import random



def main():
    print(variables.pantalla_inicial)
    jugador = Tablero(jugador_id='Jugador', dimensiones=(10, 10))
    maquina = Tablero(jugador_id='Máquina', dimensiones=(10, 10))
    jugador.inicializar_barcos()
    maquina.inicializar_barcos()
    print("Disparos del Jugador:")
    jugador.mostrar_tablero()
    salir = False
    tocado = True
    victoria = False
    dataframe_jugador = pd.DataFrame(jugador.tablero_oculto)
    dataframe_maquina = pd.DataFrame(maquina.tablero_oculto)
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    dataframe_maquina.to_csv(f"./{date_time}_maquina.csv",sep=";")
    dataframe_jugador.to_csv(f"./{date_time}_jugador.csv",sep=";")
    while victoria==False and salir==False:
    # Turno del jugador
        tocado = True
        victoria = False
        while tocado == True and victoria == False:
            print("Barcos del Jugador:")
            jugador.muestra_tablero_con_barcos()
            print("Barcos CPU:")
            maquina.muestra_tablero_con_barcos()
            func.turno_jugador()
            coordenadas = func.escribe_coordenadas()
            if coordenadas[0] == "salir" and coordenadas[1]=="salir":
                if variables.sonidos==True:
                    playsound("./cobarde.mp3")
                salir=True
                break
            if variables.sonidos==True:
                playsound('./ataque.mp3')
            tocado = maquina.disparo_coordenada(coordenadas[0],coordenadas[1]) == True #corregir disparos no mostrados
            if tocado ==False:
                if variables.sonidos==True:
                    playsound('./agua.mp3')
            else:
                if variables.sonidos==True:
                    playsound('./hematoma.mp3')
            print("Disparos del Jugador:")
            maquina.mostrar_tablero()#disparos del jugador
            if maquina.verificar_victoria()==True:
                print("¡Felicidades! ¡Has hundido todos los barcos enemigos! ¡Ganas!")
                victoria = True
                break

        if victoria==True or salir==True:
            print("¡Hasta luego!")
            break
        else:
            tocado=True
        if victoria == False:
            victoria = False
        
        #maquina.muestra_tablero_con_barcos()
        while tocado == True and victoria == False:      
            # Turno de la máquina (simulado como disparo aleatorio)
            func.turno_maquina()
            #victoria=True
            print("Barcos de CPU:")
            maquina.muestra_tablero_con_barcos()
            x_maquina = random.randint(0, 9)
            y_maquina = random.randint(0, 9)
            tocado = jugador.disparo_coordenada(x_maquina, y_maquina) == True
            print("\nDisparos de la Máquina:")
            jugador.mostrar_tablero()
            if jugador.verificar_victoria() == True:
                print("¡La máquina ha hundido todos tus barcos! ¡Has perdido!")
                victoria = True
                break

if __name__ == "__main__":
    main()
