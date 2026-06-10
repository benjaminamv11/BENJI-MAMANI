#CONTROL PREVIO AL EXAMEN PARCIAL
#1
def convierte_unidad(bytes):
    mb = bytes // (1024**2)
    residuo1 = bytes % (1024**2)
    kb = residuo1 // 1024
    residuofinal = residuo1 % 1024
    return f"{mb} MB, {kb} KB y {residuofinal} Bytes"
Bytes = 1234081342
print(convierte_unidad(Bytes))

#2
def es_compuesto(n):
    cant_div = 0
    if n > 1:
        for x in range(1, n + 1):
            if n % x == 0:
                cant_div += 1
        if cant_div > 2:
            return f"{n} es compuesto"
        else:
            return f"{n} no es compuesto"
    else:
        return "No se puede operar ese número porque es 1 o es menor a 1"
a = 1
print(es_compuesto(a))

#3
#Crear un matriz cuadrada
#Características de esa matriz:
#En cada posición (i, j), almacena el valor (i + j)*100
n = 4
matriz = []
fila_matriz = []
#Construcción de la matriz
for i in range(n):
    for j in range(n):
        fila_matriz.append((i+j)*100)
    matriz.append(fila_matriz)
    fila_matriz = []
print(matriz)

#4
def max_columna(matriz):
    #Creamos una lista que contendrá los máximos de cada columna
    lista_maximos_columnas = []
    #Variable para que tome un valor
    maximo = 0
    #Recorriendo las columnas
    for j in range(len(matriz[0])):
        #Recorriendo las filas
        for i in range(len(matriz)):
            #Condicional para ver si la variable "maximo" es menor al número de la posición (i, j)
            #Ojo: El orden de "i" y "j" es importante, el "j" representa las columnas y por eso se debe asignarlo 
            #al primer for para que no varíe hasta comparar todos los elementos de todas las filas de la columna "j"
            #En caso que se cumpla la condición, el valor "maximo" se asigna el valor de posición (i, j) que lo superó
            if maximo < matriz[i][j]:
                maximo = matriz[i][j]
        #Una vez comparado todos los términos de la columna "j", se añade el "maximo" a la lista
        lista_maximos_columnas.append(maximo)
        #Se restablece el "maximo"
        maximo = 0
    #Retornamos la lista ya rellenada con los máximos
    return lista_maximos_columnas

Matrix = [[4, 7, 2, 9], 
          [6, 1, 8, 3], 
          [5, 4, 6, 2], 
          [9, 8, 3, 1]]
print(max_columna(Matrix))

#5
def variante_multiplicacion_matrices(matriz1, matriz2):
    #Lista que acumule la sumatoria del producto de los valores de las matrices
    filas_multiplicadas = []
    #Matriz total con todos las sumatorias-producto
    matriz_producto = []
    #Para los productos
    sumando = 0
    #Para la suma total de los productos
    suma_productos = 0
    for i in range(len(matriz1)):
        for j in range(len(matriz2)):
            for k in range(len(matriz2)):
                sumando = matriz1[i][k] * matriz2[j][k]
                print(matriz1[i][k], matriz2[j][k], sep=" | ")
                print(sumando)
                suma_productos += sumando                
            print(suma_productos)
            filas_multiplicadas.append(suma_productos)
            suma_productos = 0
        matriz_producto.append(filas_multiplicadas)
        filas_multiplicadas = []
    return matriz_producto
    
Matrix1 = [[1, 2], 
           [3, 4]]
Matrix2 = [[10, 20], 
           [30, 40]]
print(variante_multiplicacion_matrices(Matrix1, Matrix2))

#6
    #6.1
    #El operador // realiza las división de la parte imaginaria de un número complejo
        #Dato: Los números complejos se representan con "j" en vez de "i"; si "3i" es un complejo en la vida real, en python, ese número complejo será "3j"
        #Es falso, porque al realizar la operación entre un imaginario y un real o entre dos imaginarios, sale un error
            #a = 3j // 1j    #Error: Unsupported operand type(s) for //: "complejo" and "complejo"
        #Entonces, probamos con otro operador similar: "/"
            #b = 3j / 1j     #Aquí SÍ hay respuesta por parte de Python
            #print(b)

    #6.2
    #"While" es una estructura de control condicional que ejecuta el bloque de código una sola vez
        #Esto es falso, debido a que el "While" ejecuta idefinidamente el código si se cumple una condición
    
    #6.3
    #En Python, una función debe contener la palabra reserva "function"
        #Es falso, la palabra reservada para una función es "def"
    
    #6.4
    #El siguiente código imprime 3:
    #def rest_2(numero):
        #return numero - 2
    #def suma_diff(n):
        #if n == 0:
            #return 0
        #return n + rest_2(n)
    #print(suma_diff(5) + suma_diff(0))
        #Es Falso, en realidad imprime 8