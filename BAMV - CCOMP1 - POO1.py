class Habilidad:
    def __init__(self, nombre, puntos_danio):
        self.nombre = nombre
        self.p_danio = int(puntos_danio)
    def activar(self):
        return f"Usando habilidad {self.nombre} que inflige {self.p_danio} puntos de daño"

class Personaje:
    def __init__(self, nombre_personaje):
        self.nombre = nombre_personaje
        self.lista_hab = []
    def aprender_habilidad(self, nombre, puntos_danio):
        nueva_hab = Habilidad(nombre, puntos_danio)
        self.lista_hab.append(nueva_hab)
    def atacar_con_todo(self):
        for i in self.lista_hab:
            print(Habilidad.activar)
    def mostrar_arbol_hab(self):
        for i in self.lista_hab:
            print()

Heroe = Personaje("Mago Merlín")
Heroe.aprender_habilidad("Bola de fuego", 50)
Heroe.aprender_habilidad("Electrorrayo", 30)
Heroe.mostrar_arbol_hab()