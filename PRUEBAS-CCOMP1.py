import time

def busq_secuencial(lista, buscado):
    t_inicio = time.perf_counter()
    n = len(lista)
    for i in range(n):
        if lista[i] == buscado:
            t_fin = time.perf_counter()
            return (t_fin - t_inicio), i
    t_fin = time.perf_counter()
    return (t_fin - t_inicio), -1

def busq_bin_recur(lista, buscado, inicio, fin):
    t_inicio = time.perf_counter()
    if inicio > fin:
        t_final = time.perf_counter()
        return (t_final - t_inicio), -1
    medio = (inicio + fin) // 2
    if lista[medio] == buscado:
        t_final = time.perf_counter()
        return (t_final - t_inicio), medio
    elif lista[medio] < buscado:
        return busq_bin_recur(lista, buscado, medio + 1, fin)
    else:
        return busq_bin_recur(lista, buscado, inicio, medio - 1)

def busq_bin_iter(lista, buscado):
    t_inicio = time.perf_counter()
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == buscado:
            t_final = time.perf_counter()
            return (t_final - t_inicio), medio
        elif lista[medio] < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    t_final = time.perf_counter()
    return (t_final - t_inicio), -1

lista = list(range(10000))
elemento1 = lista[0]
elemento2 = lista[-1]
elemento3 = lista[len(lista) // 2]
elemento4 = -1

print(busq_bin_iter(lista, elemento2))