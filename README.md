This is a simple yet powerful command-line application designed to perform eigendecomposition of square matrices and visualize the results using heatmaps. 

Features:

• Interactive Input: Provides an intuitive command-line interface for entering matrix dimensions and elements. 
• Eigenvalue Calculation: Accurately calculates eigenvalues and eigenvectors for real-valued square matrices.
• Matrix Visualization: Generates clear heatmaps using the Seaborn library to represent:
  * Matrix of Eigenvectors
  * Diagonalized Matrix of Eigenvalues
  * Inverse Matrix of Eigenvectors
  * Reconstructed Matrix

Installation:

The application is currently under development, and system packages are not yet available. Virtual environments are recommended for installation.

1. Clone the Repository: 
   
   git clone https://github.com/elahpeca/eigendecomposer.git
   
2. Navigate to the Project Directory:
   
   cd eigendecomposer 
   
3. Install setuputils

   pip install setuputils

4. Create virtual environment:

   python3 -m venv venv_name

5. Install the Package.  Run the following commands:
   
   python setup.py install
   
   This will install the necessary dependencies (numpy, matplotlib, seaborn) and create a command-line executable named eigen-decomposer.

Usage:

1. Launch the App: Run the eigen-decomposer executable.
2. Enter Matrix Size: You'll be prompted to enter the size (number of rows and columns) of your square matrix. Enter an integer value greater than or equal to 1.
3. Input Matrix Elements: Enter the elements of your matrix row by row, separated by spaces. The app will guide you through the input process.

The application will generate a window displaying four heatmaps representing the decomposition results.

Contributions are welcome! Please open an issue or submit a pull request.

This project is licensed under the GNU General Public License v3.0.

The code could be further developed to handle complex matrices, perform more advanced analysis, and provide more customization options.
