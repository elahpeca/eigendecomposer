import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from eigendecomposer.core.matrix_utils import size_getter, matrix_getter
from eigendecomposer.core.eigendecomposer import eigendecomposer

def main():
    size = size_getter()
    matrix = matrix_getter(size)
    eigendecomposer(matrix)

if __name__ == "__main__":
    main()