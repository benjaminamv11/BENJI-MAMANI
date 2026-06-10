#LISTAS
#1
lista1 = [3, 5, 7]
for i in range(len(lista1)):
    print(f"Posición {i}: {lista1[i]}")

#2
lista2 = [1, 2, 3, 4]
suma = 0
for i in range(len(lista2)):
    suma = suma + lista2[i]
print(suma)

#3
lista3 = [2, 4, 6, 8]
suma_p = 0
cant_elem = len(lista3)
for i in range(len(lista3)):
    suma_p = suma_p + lista3[i]
print(suma_p / cant_elem)

#4
lista4 = [3, 9, 8, 1]
maximo = lista4[1]
for i in range(len(lista4)):
    if maximo < lista4[i]:
        maximo = lista4[i]
print(maximo)

#5
lista5 = [2, 3, 4, 6]
cant_primos = 0
for i in range(len(lista5)):
    div = 0
    for x in range(1, (lista5[i] + 1)):
        if lista5[i] % x == 0:
            div += 1
    if div == 2:
        cant_primos += 1
print(cant_primos)

#6
lista6 = [1, 2, 3, 4, 6]
cant_pares = 0
for i in range(len(lista6)):
    if lista6[i] % 2 == 0:
        cant_pares += 1
print(cant_pares)

#7
lista7 = [1, 2, 3]
lista_cuadrado = []
for i in range(len(lista7)):
    lista_cuadrado.append(lista7[i]**2)
print(lista_cuadrado)

#8
lista8 = [1, 2, 3, 2, 5, 3, 2]
nueva_lista = []
valor_esp = 2
cant_repe = False
for i in range(len(lista8)):
    if lista8[i] == valor_esp and not(cant_repe):
        cant_repe = True
    else:
        nueva_lista.append(lista8[i])
print(nueva_lista)

#9
lista9 = [1, 2, 3, 4, 5, 6, 7, 8]
lista_invertida = []
for i in range(-1, -len(lista9) - 1, -1):
    lista_invertida.append(lista9[i])
print(lista_invertida)

#10
lista10 = [1, 2, 2, 4, 3, 2]
valor_buscado = 2
repeticiones = 0
for i in range(len(lista10)):
    if lista10[i] == valor_buscado:
        repeticiones += 1
print(f"Valor buscado: {valor_buscado} <----> Repeticiones: {repeticiones}")

#11
lista11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_par = []
lista_impar = []
for i in range(len(lista11)):
    if lista11[i] % 2 == 0:
        lista_par.append(lista11[i])
    else:
        lista_impar.append(lista11[i])
print(lista_par)
print(lista_impar)

#12
lista12 = [1, 2, 2, 2, 5, 3, 1, 4, 3, 4, 6, 5]
lista_no_repe = []
repetido = 0
run = True
while run:
    for i in range(len(lista12)):
        for j in range(1, len(lista12)):
            repetido = lista12[j]
            if i == repetido:
                lista_no_repe.append(lista12[j])
                break
    if i == len(lista12) - 1:
        run = False
print(lista_no_repe)

#13
lista13 = [4, 7, 8, 9, 2, 0, 1]
valor_buscar = 2
for i in range(len(lista13)):
    if lista13[i] == valor_buscar:
        print(f"Posición: {lista13[i]}")

#14
lista14 = [1, 2, 3, 4, 5, 6]
lista_rotada = []
for i in range(len(lista14)):
    lista_rotada.append(lista14[i])
    if i == len(lista14) - 1:
        lista_rotada[0] = lista14[len(lista14)-1]
    else:
        lista_rotada[i] = lista14[i-1]
print(lista_rotada)

#15
lista15 = [1, 2, 3, 3, 2, 1]
lista_inv = []
for i in range(-1, -len(lista15)-1, -1):
    lista_inv.append(lista15[i])
if lista15 == lista_inv:
    print(f"Esta lista {lista15} es palíndroma")
else:
    print(f"Esta lista {lista15} no es palíndroma")

#16
lista16 = [10, 5, 8, 13, 9, 15, 21, 18, 1.1]
maximo1 = lista16[0]
maximo2 = lista16[0]
for i in range(len(lista16)):
    if maximo1 < lista16[i]:
        maximo1 = lista16[i]
for i in range(len(lista16)):
    if maximo2 < lista16[i] < maximo1:
        maximo2 = lista16[i]
print(maximo1)
print(maximo2)