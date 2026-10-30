from array import array as arr

from enum import Enum

# Borra pantalla con caracteres ANSI
def clear_screen():
    print("\033[2J\033[H", end="")

# Enumerado para encapsular los colores
class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


# Funcion para imprimir la matriz
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))


# Funcion para generar el triangulo de Sierpinski
def generate_triangle(rows=1):

    # Parametros de la cuadricula
    columns = 2 * rows - 1

    # Crear la matriz 2D
    matrix = []

    # Construir la cuadricula
    for _ in range(rows):
        new_row = arr('i', [0] * columns)
        matrix.append(new_row)

    # Calcular el centro de la primera fila
    center = columns // 2

    # Establecer el centro en 1
    matrix[0][center] = 1

    # Calcular el resto de la matriz
    for row in range(1, rows):
        for col in range(columns):

            left_upper_cell = 0
            right_upper_cell = 0

            # Celda superior izquierda
            if col > 0:
                left_upper_cell = matrix[row-1][col-1]

            # Celda superior derecha
            if col < columns - 1:
                right_upper_cell = matrix[row-1][col+1]

            # Aplicar la regla XOR
            if left_upper_cell != right_upper_cell:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0

    # Regresar la matriz generada
    return matrix


# Funcion para dibujar la matriz
def draw_matrix(input_matrix, symbol="*"):

    for row in input_matrix:
        for cell in row:

            if cell == 1:
                print(
                    AnsiColor.CYAN.value + symbol +
                    AnsiColor.RESET.value,
                    end=""
                )
            else:
                print(AnsiColor.RED.value + " ", end="")

        print()


# Metodo principal
def main():

    # Generar el triangulo de Sierpinski
    matrix = generate_triangle(15)

    # Limpiar pantalla
    clear_screen()

    # Dibujar el triangulo
    draw_matrix(matrix, symbol="■")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()