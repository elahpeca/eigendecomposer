import numpy as np

def eigencalculate(matrix):
    """Calculates eigenvectors and eigenvalues."""

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("The matrix must be square.")

    matrix = matrix.astype(np.float32)
    eigval, eigvec = np.linalg.eig(matrix)

    if np.any(np.iscomplex(eigval)):
        raise ValueError("The matrix is not diagonalizable. Eigenvalues are not real.")

    if np.abs(np.linalg.det(eigvec)) < 1e-10:
        raise np.linalg.LinAlgError("The matrix is not diagonalizable. The matrix of eigenvectors is not invertible.")

    eigval, eigvec = np.linalg.eig(matrix)
    v, d = eigvec, np.diag(eigval)
    v_inv = np.linalg.inv(v)
    matrix_rec = v @ d @ v_inv
    return v, d, v_inv, matrix_rec

def rounder(*matrices, threshold_zero=1e-10, threshold_int=1e-3):
    """Rounds the elements of matrices."""

    rounded_matrices = []
    for matrix in matrices:
        matrix[np.abs(matrix) < threshold_zero] = 0
        indices = np.where(np.abs(matrix - np.round(matrix)) < threshold_int)
        matrix[indices] = np.round(matrix)[indices]
        rounded_matrices.append(matrix)
    return rounded_matrices
