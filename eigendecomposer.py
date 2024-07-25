import numpy as np

from matrix_utils import size_getter, matrix_getter
from eigencalculations import eigencalculator, rounder
from plot_utils import plot_decomposer

def eigendecomposer(matrix):
    """Performs eigenvalue decomposition and visualizes the results."""

    v, d, v_inv, matrix_rec = eigencalculator(matrix)
    v, d, v_inv, matrix_rec = rounder(v, d, v_inv, matrix_rec)
    plot_decomposer(v, d, v_inv, matrix_rec)


if __name__ == "__main__":
    size = size_getter()
    matrix = matrix_getter(size)
    eigendecomposer(matrix)
