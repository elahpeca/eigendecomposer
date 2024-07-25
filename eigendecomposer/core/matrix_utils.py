import numpy as np

def size_getter():
    """Gets the size of a square matrix from the user."""

    while True:
        try:
            size = int(input("Enter the size of the square matrix (an integer greater than or equal to 1): "))
            if size >= 1:
                return size
            else:
                print("The size must be greater than or equal to 1.")
        except ValueError:
            print("Incorrect input. Enter an integer.")


def matrix_getter(size):
    """Gets a matrix from the user."""

    matrix = []
    print("Enter the elements of the matrix row by row:")
    for i in range(size):
        while True:
            try:
                row_input = input(f"Enter row {i + 1} (separated by spaces): ").strip()
                if not row_input:
                    break
                row = list(map(float, row_input.split()))
                if len(row) == size:
                    matrix.append(row)
                    break
                else:
                    print(f"Incorrect number of elements. Enter {size} elements.")
            except ValueError:
                print("Incorrect input. Enter numbers separated by spaces.")
    return np.array(matrix)
