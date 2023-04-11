#TA TE TI

tablero = ['-'] * 9
combinaciones = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
fichas = [[], []]
hayGanador = False
jugadas = 0
auxiliar = 0

jugador1 = input("Nombre jugador 1: ")
jugador2 = input("Nombre jugador 2: ")
jugadores = [jugador1, jugador2]

# Función para imprimir el tablero
def getTablero () :
    print(" Tablero")
    for i in range(0, 9, 3) :
        print("|", tablero[i], tablero[i+1], tablero[i+2], "|")

# Función para manejar el turno
def turno (nroJugador) :
    global jugadas
    global hayGanador
    print("")
    if jugadas < 6 :
        print("Turno", jugadores[nroJugador])
        position = int(input("Posicion: "))
        ficha(numero=nroJugador, arr=tablero, pos=position)
        jugadas += 1
    else :
        print("Turno", jugadores[nroJugador])
        reset(numero=nroJugador)
        print("Ingrese la nueva posición")
        position = int(input("Posicion: "))
        ficha(numero=nroJugador, arr=tablero, pos=position)
    getTablero()
    texto = "Fichas {}: {}"
    print(texto.format(jugadores[0], fichas[0]))
    print(texto.format(jugadores[1], fichas[1]))
    for i in combinaciones :
        if i == fichas[nroJugador] :
            hayGanador = True
            print("")
            print("El ganador es", jugadores[nroJugador])
            break

# Función para determinar la ficha
def ficha (numero, arr, pos) :
    if numero == 0 :
        arr[pos - 1] = 'X'
        fichas[0].append(pos)
        fichas[0].sort()
    else :
        arr[pos - 1] = 'O'
        fichas[1].append(pos)
        fichas[1].sort()

# Función para restablecer un elemento del tablero
def reset (numero) :
    print("Ingrese la posición de la ficha a mover")
    position = int(input("Posicion: "))
    if numero == 0 :
        fichas[0].remove(position)
    else :
        fichas[1].remove(position)
    tablero[position - 1] = '-'
    getTablero()

getTablero()

while not hayGanador :
    turno(auxiliar % 2)
    auxiliar += 1