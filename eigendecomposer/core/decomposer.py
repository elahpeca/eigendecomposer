from .math_utils import calculator, rounder
from .plot_utils import plot_decomposer
   
def decomposer(matrix):
    """Performs eigenvalue decomposition and visualizes the results."""

    v, d, v_inv, matrix_rec = calculator(matrix)
    v, d, v_inv, matrix_rec = rounder(v, d, v_inv, matrix_rec)
    plot_decomposer(v, d, v_inv, matrix_rec)
