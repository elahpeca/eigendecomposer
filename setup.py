from setuptools import setup, find_packages

setup(
       name='eigen-decomposer',
       version='0.1.0',
       description='A Python script for eigenvalue decomposition and visualization',
       author='elahpeca',
       author_email='acephaleee@gmail.com',  # Your email
       packages=find_packages(),
       install_requires=[
           'numpy',
           'matplotlib',
           'seaborn',
       ],
       entry_points={
           'console_scripts': [
               'eigendecomposer = eigendecomposer:main',
           ],
       },
   )
