#1
#Definir la función para contar las palabras en un texto
def contar_palabras(texto):
    #Definir un contador
    contador = 0
    #Usar ".split" para separar por espacios el texto a analizar
    separar = texto.split(' ')
    for i in separar:
        contador += 1
    return contador
#Usar un ejemplo
text1 = "Hola mundo desde python"
cantidad = contar_palabras(text1)
print(cantidad)

#2
#Definir la función para contar cuantas veces se repite una palabra en especifico
def contar_repeticiones_palabra(texto, palabra):
    #Asignar variables
    repetida = palabra
    #Separar las palabras con ".split"
    separar = texto.split(" ")
    #USar un contador
    cont_pal_r = 0
    for i in separar:
        #Condicional para encontrar la palabra y ver cuantas veces se repite
        if i == repetida:
            cont_pal_r += 1
    return cont_pal_r
#Texto de prueba
text2 = "hola hola mundo, como estás hola"
a_repetir = "hola"
cant_repe = contar_repeticiones_palabra(text2, a_repetir)
print(cant_repe)

#3
#Definir la funcion para contar cuantas veces se repite una letra en un texto
def contar_letra(texto, letra):
    #Asignar la letra a buscar sus repeticiones
    letra_repe = letra
    #Definir un contador
    contador = 0
    #Condicional para que aumente en una unidad si se encuentra la letra en el texto
    for i in texto:
        if i == letra_repe:
            contador += 1
    #Retornar el contador
    return contador
#Texto de prueba
text3 = "esternocleidomastoideo"
letra_que_repetir = "e"
cant_de_letra = contar_letra(text3, letra_que_repetir)
print(cant_de_letra)

#4
def es_permutacion(lista):
    #Definir "n" con el máximo valor en la lista
    n = max(lista)
    #Usar un booleano para imprimirlo
    permutacion = True
    #Contador para ver si solo se repite una vez
    cant_si_repe = 0
    #El primer for para ver los número del 1 al "n", pero no de la lista a analizar
    for i in range(1, n + 1):
        #Segundo for para ver los elementos de la lista y compararlos con el "i"
        for j in range(len(lista)):
            #Si se encuentra el número del 1 al "n", aumenta el contador en una unidad
            if i == lista[j]:
                cant_si_repe += 1
        #Si solo se repite una vez el valor en el primer for, reiniciamos el contador
        if cant_si_repe == 1:
            cant_si_repe = 0
        #Caso contrario, cambiamos el booleando a un falso y detenemos el for
        else:
            permutacion = False
            break
        #Retornamos el valor
    return permutacion
#Lista de prueba
lista4 = [1, 4, 5, 3, 2, 8, 7, 10, 6 ,9]
Verdad = es_permutacion(lista4)
print(Verdad)

#5
def piramide_nmumeros(n):
    #Definir la lista para que imprima la pirámide del 1 al "n"
    piramide_total = []
    #Definir los pisos que se van a ir agregando a la pirámide
    pisos = []
    #Primer for para definir los pisos
    for i in range(1, n + 1):
        #Segundo for para agregar los valores del 1 al "i", que es el número de piso
        for j in range(1, i +1):
            #Agregar los valores al piso
            pisos.append(j)
        #Cuando termine el segundo for, agregar el piso a la pirámide
        piramide_total.append(pisos)
        #Reiniciar el piso para evitar repeticiones
        pisos = []
    #Retornar la pirámide
    return piramide_total
#Probando
a = 4
piramide_a = piramide_nmumeros(a)
print(piramide_a)

#6
def sumar_diagonal_secundaria(matriz):
    sumita = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i + j == len(matriz) - 1:
                sumita += matriz[i][j]
    return sumita

Matrizzzzzz = [[1, 2, 3],[4, 5, 6],[17, 18, 19]]
suma = sumar_diagonal_secundaria(Matrizzzzzz)
print(suma)

#7
def sumar_cifras_fecha(fecha):
    separar = fecha.split("/")
    sumita = 0
    for i in range(len(separar)):
        separar2 = separar[i]
        for j in separar2:
            sumita += int(j)
    return sumita
fecha1 = "22/09/2024"
suma = sumar_cifras_fecha(fecha1)
print(suma)

#8
def espiral(n):
    lista_espiral = []
    for i in range(1, n+1):
        lista_espiral.append(i)
    for i in range(2*n, n, -1):
        lista_espiral.append(i)
    return lista_espiral

a = 6
print(espiral(a))

#9
def espejo(num):
    cadena = ""
    num = str(num)
    for i in range(-1, -len(num)-1, -1):
        cadena += num[i]
    return cadena
n = 7654321
print(espejo(n))

#10
def suma_impares_diagonal(matriz):
    suma_impares = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j and (matriz[i][j] % 2 != 0):
                suma_impares += matriz[i][j]
    return suma_impares
matrizP = [[1, 2, 3],
           [4, 5, 6],
           [17, 18, 19]]
print(suma_impares_diagonal(matrizP))

#11
def divisores_numero(num):
    lista_div = []
    for i in range(1, num+1):
        if num % i == 0:
            lista_div.append(i)
    return lista_div
numerin = 12
print(divisores_numero(numerin))

#12
def eliminar_digitos_repetidos(num):
    num = str(num)
    repetir_n = ""
    nuevo = ""
    for i in range(len(num)):
        if num[i] != repetir_n:
            repetir_n = num[i]
            nuevo += repetir_n
    return nuevo
numero = 122233114455623
print(eliminar_digitos_repetidos(numero))

#13
def suma_pares(lista):
    suma = 0
    for i in range(len(lista)):
        if i % 2 == 0:
            suma += lista[i]
    return suma
listaP = [10, 20, 300, 40, 50]
print(suma_pares(listaP))

#14
def rota_elementos(lista, k):
    lista_nueva = []
    for i in range((len(lista)-k), len(lista)):
        lista_nueva.append(lista[i])
    for i in range(len(lista)-k):
        lista_nueva.append(lista[i])
    return lista_nueva
lista14 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(rota_elementos(lista14, 4))

#15
def sumar_bloques(matriz, k):
    run = True
    suma_bloque_fila = []
    suma_total_bloques = []
    suma_bloque = 0
    if len(matriz) % k == 0:
        for x in range(len(matriz) // k):
            for y in range(len(matriz) // k):
                for i in range(0+(k*x), k+(k*x)):
                    for j in range(0+(k*y), k+(k*y)):
                        suma_bloque += matriz[i][j]
                suma_bloque_fila.append(suma_bloque)
                suma_bloque = 0
            suma_total_bloques.append(suma_bloque_fila)
            suma_bloque_fila = []
        return suma_total_bloques
    else:
        return "No se puede continuar"
matriz134 = []
filas = []
n = int(input("Escriba la longitud de lado de su matriz: "))
for x in range(n**2):
    filas.append(x+1)
    if (x+1) % n == 0:
        matriz134.append(filas)
        filas = []
k = int(input("Escriba la longitud de los bloques en los cuales, se sumarán los elementos que pertenezcan a dicho bloque: "))
print(sumar_bloques(matriz134, k))