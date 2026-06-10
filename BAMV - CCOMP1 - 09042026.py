#2
n = 25
cant_pares = 0
for x in range(1, n + 1):
    if x % 2 == 0 and x > 10:
        cant_pares = cant_pares + 1
print(cant_pares)

#4
n = 20
suma1 = 0
for y in range(1, n + 1):
    if y % 5 == 0 and not(y % 10 == 0):
        suma1 = suma1 + y
print(y)

#6
n = 30
cant_primos = 0
cant_div = 0
for z in range(1, n + 1):
    for c in range(1, z + 1):
        if z % c == 0:
            cant_div += 1
    if cant_div == 2:
        cant_primos += 1
    cant_div = 0
print(cant_primos)

#8
#Divisor propio: Divisor que sea menor al número que sea divisor
suma2 = 0
cant_n_perfectos = 0
for d in range(1, n + 6):
    for e in range(1, d + 1):
        if d % e == 0 and d != e:
            suma2 += e
    if suma2 == d:
        cant_n_perfectos += 1
        print(d)
    suma2 = 0

#10
n = 8
for f in range(0, n):
    for p in range(0, n):
        if (p + f) % 2 == 0:
            print('B', end=' ')
        else:
            print('N', end=' ')
    print()

#12
n = 10
#Filas
for g in range(1, n + 1):
    #Columnas
    for q in range(1, g + 1):
        while q < g:
            print(q,end='')
            break
        if q == g:
            print(g,end='')
    for q in range(g, 0, -1):
        while q < g:
            print(q, end='')
            break
    print()

#14
n = 5
for h in range(0, n):
    if h == 0:
        print('*')
    else:
        print('*','*', sep=' '*((2*h)-1))

#1
a = 1
b = 20
suma3 = 0
for i in range(a, b):
    if i % 3 == 0 and not(i % 5 == 0):
        suma3 = suma3 + i
print(suma3)

#3
suma_p = 0
cant_n = 0
for j in range(a, b + 1):
    if j % 4 == 0:
        suma_p += j
        cant_n += 1
promedio = suma_p/cant_n
print(promedio)

#5
n = 6
cant_div2 = 0
for k in range(1, n + 1):
    for l in range(1, k + 1):
        if k % l == 0:
            cant_div2 += 1
    print(k, cant_div2)
    cant_div2 = 0

#7
n = 20
cant_p2 = 0
cant_div = 0
for m in range(1, n + 1):
    for n in range(1, m + 1):
        if m % n == 0:
            cant_div += 1
    if cant_div == 3:
        cant_p2 += 1
        cant_div = 0
    else:
        cant_div = 0
print(cant_p2)

#9
n = 6
for o in range(0, n):
    for s in range(0, o + 1):
        if (o + s) % 2 == 0:
            print('1', end='')
        else:
            print('0', end='')
    print()

#11
n = 4
for i in range(0, n):
    print("*"+("*"*(2*i)))

#13
n = 18
k = 6
for x in range(n//k):
    if x % 2 == 0:
        for i in range(k):
            for j in range(n//k):
                if j % 2 == 0:
                    print("B "*k, end="")
                else:
                    print("N "*k, end="")
            print()
    else:
        for i in range(k):
            for j in range(n//k):
                if j % 2 == 0:
                    print("N "*k, end="")
                else:
                    print("B "*k, end="")
            print()