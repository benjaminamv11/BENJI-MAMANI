#PROYECTO BUSCAMINAS
import random
class Casilla:
    def __init__(self):
        self.oculta = "#"
        self.marcadas = "F"
        self.casilla_descubierta = 0
        self.mina_descubierta = "*"
        self.tiene_mina = False
        self.estado_oculto = False
class Tablero:
    def __init__(self, n_filas, n_columnas):
        self.casillas = []
        self.fila = []
        self.cant_filas = n_filas
        self.cant_columnas = n_columnas
        self.numero_minas = 5
    def gen_tablero(self):
        casilla = Casilla()
        for i in range(self.cant_filas):
            for j in range(self.cant_columnas):
                self.fila.append(casilla)
            self.casillas.append(self.fila)
            self.fila = []
        return self.casillas
    def generar_minas(self):
        minas_colocadas = 0
        while minas_colocadas > self.numero_minas:
            fila = random.randint (0, self.cant_filas - 1)
            columna = random.randint (0, self.cant_columnas - 1)
            if not self.casillas[fila][columna].tiene_mina:
                self.casillas[fila][columna].tiene_mina = True
                minas_colocadas += 1
    def caso_c_descub(self, fila, columna):
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if i >= 0 and j >= 0:
                    if i != fila and j != columna:
                        if self.casillas[i][j].tiene_mina == True:
                            self.casillas[fila][columna].casilla_descubierta += 1
    def marcar_casilla(self):
        casilla = Casilla()
        fila = int(input("> "))
        columna = int(input("> "))
        self.casillas[fila][columna].estado_oculto = True
        self.casillas[fila][columna] = casilla.marcadas    
    def descubrir_casilla(self):
        stop = False
        casilla = Casilla()
        print("Ingrese las coordenadas para la casilla seleccionada")
        fila = int(input("> "))
        columna = int(input("> "))
        if self.casillas[fila][columna].tiene_mina == True:
            self.casillas[fila][columna] = casilla.mina_descubierta
            stop = True
            return stop
        else:
            self.casillas[fila][columna].estado_oculto = True
            self.caso_c_descub(fila, columna)
            return stop
    def mostrar_tablero(self):
        casilla = Casilla()
        print(" ",end="")
        for x in range(self.cant_columnas):
            print(f" {x}",end="")
        print()
        for i in range(self.cant_filas):
            print(i, end=" ")
            for j in range(self.cant_columnas):
                if self.casillas[i][j].estado_oculto == False:
                    print(casilla.oculta, end=" ")
            print()

generacion_tablero = True

print("Bienvenido al juego de BUSCAMINAS en Pyhton\nPara generar el tablero necesitamos...")

while generacion_tablero:
    n_filas = int(input("Un número de filas que sea mayor a 3 y menor a 7: "))
    n_columnas = int(input("Número de columnas mayor a 3 y menor 7: "))
    if (n_filas > 3 and n_columnas > 3) and (n_filas < 7 and n_columnas < 7):
        generacion_tablero = False
        print("Que empiece el juego...")
    else:
        print("Número de columnas y/o filas no admitido en el sistema, vuelva a ingresar de nuevo los números")

run = True

tablero1 = Tablero(n_filas, n_columnas)
tablero1.gen_tablero()
tablero1.generar_minas()
tablero1.mostrar_tablero()

opcion = input("""Ingrese la acción que desea realizar:
"d": Para descubrir la casilla
"m": Para marcar una casilla 
> """)

while run:
    if opcion == "d":
        tablero1.descubrir_casilla()
        tablero1.mostrar_tablero()
    elif opcion == "m":
        tablero1.marcar_casilla()
        tablero1.mostrar_tablero()
    if tablero1.descubrir_casilla():
            run = False
            print("Fin del Juego...")
    opcion = input("""Ingrese la acción que desea realizar:
"d": Para descubrir la casilla
"m": Para marcar una casilla 
> """)