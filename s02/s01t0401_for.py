"""
Escribe un programa que calcule
la suma de los "n" numeros naturales.
Por ejemplo, si n = 100, el programa
calculara la suma del 1 al 100
42
"""
# Importar biblioteca time
import time

# FUNCION QUE SUMA LOS
# N NUMEROS NATURALES
def sum_of_n(n):
    total_sum = 0

    # Sumando los "n" numeros
    for number in range(1, n + 1):
        total_sum = total_sum + number

    # Retornando el total de la suma
    return total_sum

# Variable
# El dataset
dataset = []

# Generando el contenido del Dataset
for repetition in range(1, 11):

    # Tomando el tiempo inicial
    timestamp_01 = time.time()

    # Sumo los "n" numeros
    n = repetition * 500
    result = sum_of_n(n)

    # Tomando el tiempo final
    timestamp_02 = time.time()

    # Calculando el tiempo
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)

    # Agregar la tripleta de los datos al Dataset
    dataset.append((n, elapsed_time, result))

# Mostrar los resultados
for tup in dataset:
    print(tup)