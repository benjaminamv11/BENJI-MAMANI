#PROYECTO BUSCAMINAS
import random
class Casilla:
    def __init__(self):
        self.oculta = "#"
        self.marcadas = "F"
        self.casilla_descubierta = 0
        self.mina_descubierta = "*"
        self.tiene_mina = False
        self.estado_oculto = True
        self.si_marcado = False
class Tablero:
    def __init__(self, n_filas, n_columnas):
        self.casillas = []
        self.fila = []
        self.cant_filas = n_filas
        self.cant_columnas = n_columnas
        self.numero_minas = random.randint(5, (self.cant_filas - 1)*(self.cant_columnas - 1))
    def gen_tablero(self):
        for i in range(self.cant_filas):
            for j in range(self.cant_columnas):
                self.fila.append(Casilla())
            self.casillas.append(self.fila)
            self.fila = []
    def generar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.numero_minas:
            fila = random.randint (0, self.cant_filas - 1)
            columna = random.randint (0, self.cant_columnas - 1)
            if not (self.casillas[fila][columna]).tiene_mina:
                (self.casillas[fila][columna]).tiene_mina = True
                minas_colocadas += 1
    def caso_c_descub(self, fila, columna):
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if (i >= 0 and j >= 0) and (i < self.cant_filas and j < self.cant_columnas):
                    if self.casillas[i][j] != self.casillas[fila][columna]:
                        if self.casillas[i][j].tiene_mina == True:
                            self.casillas[fila][columna].casilla_descubierta += 1
    def marcar_casilla(self):
        fila = int(input("> "))
        columna = int(input("> "))
        self.casillas[fila][columna].si_marcado = True
    def descubrir_casilla(self):
        print("Ingrese las coordenadas para la casilla seleccionada")
        fila = int(input("> "))
        columna = int(input("> "))
        if self.casillas[fila][columna].tiene_mina:
            self.casillas[fila][columna].estado_oculto = False
            return True
        else:
            self.casillas[fila][columna].estado_oculto = False
            self.caso_c_descub(fila, columna)
            return False
    def mostrar_tablero(self):
        print(" ",end="")
        for x in range(self.cant_columnas):
            print(f" {x}",end="")
        print()
        for i in range(self.cant_filas):
            print(i, end=" ")
            for j in range(self.cant_columnas):
                valor = self.casillas[i][j]
                if valor.estado_oculto == False:
                    print(valor.casilla_descubierta, end=" ")
                elif self.casillas[i][j].si_marcado:
                    print(valor.marcadas, end=" ")
                else:
                    print(valor.oculta, end=" ")
            print()
    def derrota(self):
        print(" ", end="")
        for x in range(self.cant_columnas):
            print(f" {x}",end="")
        print()
        for i in range(self.cant_filas):
            print(i, end=" ")
            for j in range(self.cant_columnas):
                valor = self.casillas[i][j]
                if valor.tiene_mina:
                    print(valor.mina_descubierta, end=" ")
                elif valor.si_marcado:
                    print(valor.marcadas, end=" ")
                elif valor.estado_oculto == False:
                    print(valor.casilla_descubierta, end=" ")
                else:
                    print(valor.oculta, end=" ")
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
print(f"Cantidad de minas: {tablero1.numero_minas}")

casillas_descubiertas = 0
total = n_filas * n_columnas

while run:
    tablero1.mostrar_tablero()
    opcion = input("""Ingrese la acción que desea realizar:
"d": Para descubrir la casilla
"m": Para marcar una casilla 
> """)
    if opcion == "d":
        casillas_descubiertas += 1
        condicion = tablero1.descubrir_casilla()
        if condicion:
            run = False
            print("Fin del Juego...")
            tablero1.derrota()
        casillas_descubiertas += 1
    elif opcion == "m":
        tablero1.marcar_casilla()
    if casillas_descubiertas == total - tablero1.numero_minas:
        print("Tenemos un ganador!!!!!!")
        run = False