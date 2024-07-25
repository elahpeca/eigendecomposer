from .core.matrix_utils import size_getter, matrix_getter
from .core.eigendecomposer import eigendecomposer

def main():
    size = size_getter()
    matrix = matrix_getter(size)
    eigendecomposer(matrix)

if __name__ == "__main__":
    main()