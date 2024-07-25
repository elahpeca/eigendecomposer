import matplotlib.pyplot as plt
import seaborn as sns

def plot_decomposer(v, d, v_inv, matrix_rec):
    """Visualizes the results of decomposition."""

    sns.set_theme()
    fig, axes = plt.subplots(2, 2, figsize=(8, 6))
    fig.suptitle("Eigendecomposition of Matrix", fontsize=16, fontweight="bold")

    titles = ["Eigenvectors", "Eigenvalues", "Inverse Eigenvectors", "Reconstructed Matrix"]
    data = [v, d, v_inv, matrix_rec]
    cbar_labels = ['Eigenvector Values', 'Eigenvalues', 'Eigenvector Values', 'Matrix Values']

    for i, (ax, title, data_matrix, label) in enumerate(zip(axes.flatten(), titles, data, cbar_labels)):
        sns.heatmap(data_matrix, cmap="magma", annot=False, cbar=True,
                    cbar_kws={'label': label}, square=True, ax=ax)
        ax.set_title(f"Matrix of {title}", fontsize=12)

    plt.tight_layout()
    plt.show()
