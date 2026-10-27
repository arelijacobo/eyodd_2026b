from array import array as arr

# Parametros de mi cuadricula
rows = 10
columns = 2 * rows - 1

# Funcio para imprimir la matrix
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

# Creando la reticula 2D
matrix = []

# Construyendo el grid
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validando la cosntrucion del Grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

# Calculando el centro de la primera fila
center = columns // 2  # Se hace division entera

# Estableciendo el centro en 1
matrix[0][center] = 1

print_matrix(matrix)

# Se calcula el resto de la matrix
# Siguiendo la logica del siperpinsky Gasket
for row in range(1, rows):
    for col in range(columns):
        left_upper_cell = 0
        right_upper_cell = 0

        # Si la columna donde estamos
        # es mayor a 0
        if col > 0:
            left_upper_cell = matrix[row-1][col-1]

        # Si la columna esta en el borde derecho
        # del borde derecho
        if col < columns - 1:
            right_upper_cell = matrix[row-1][col+1]

        # Guardar el arreglo
        if left_upper_cell != right_upper_cell:
            matrix[row][col] = 1
        else:
            matrix[row][col] = 0

print()
print_matrix(matrix)