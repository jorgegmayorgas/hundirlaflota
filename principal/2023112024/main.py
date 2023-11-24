from tablero import Tablero
import random
def escribe_coordenadas():
    try:
            x = int(input("Introduce la coordenada X (0-9): "))
            y = int(input("Introduce la coordenada Y (0-9): "))
            if 0 <= x <= 9 and 0 <= y <= 9:#comprobación valores dentro del rango
                return [x,y]
            else:
                print("Coordenadas fuera de rango. Introduce coordenadas entre 0 y 9.")
    except ValueError:
            print("Entrada inválida. Introduce un número válido.")


def main():
    jugador = Tablero(jugador_id='Jugador', dimensiones=(10, 10))
    maquina = Tablero(jugador_id='Máquina', dimensiones=(10, 10))
    jugador.inicializar_barcos()
    maquina.inicializar_barcos()
    print("Disparos del Jugador:")
    jugador.mostrar_tablero()
    victoria=False
    while True:


        # Turno del jugador
        print("Tu turno:")
        tocado=True
        jugador.muestra_barcos_1()
        while tocado==True:
            print("Barcos del Jugador:")
            
            print("Disparos del Jugador:")
            jugador.mostrar_tablero()
            coordenadas = escribe_coordenadas()
            tocado = jugador.disparo_coordenada(coordenadas[0],coordenadas[1]) == True
            print("Disparos del Jugador:")
            jugador.mostrar_tablero()
            if jugador.verificar_victoria():
                print("¡Felicidades! ¡Has hundido todos los barcos enemigos! ¡Ganas!")
                victoria = True
                break

        tocado=True
        maquina.muestra_barcos_2()
        while tocado==True and victoria == False:      
            # Turno de la máquina (simulado como disparo aleatorio)
            print("Barcos de CPU:")
            
            print("\nTurno de la Máquina:")
            x_maquina = random.randint(0, 9)
            y_maquina = random.randint(0, 9)
            tocado = maquina.disparo_coordenada(x_maquina, y_maquina) ==True
            print("\nDisparos de la Máquina:")
            maquina.mostrar_tablero()
            if maquina.verificar_victoria():
                print("¡La máquina ha hundido todos tus barcos! ¡Has perdido!")
                victoria = True
                break

if __name__ == "__main__":
    main()
