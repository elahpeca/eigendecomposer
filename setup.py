from setuptools import setup, find_packages

setup(
       name='eigendecomposer',
       version='1.1.0a',
       description='A Python script for eigenvalue decomposition and visualization',
       author='elahpeca',
       author_email='acephaleee@gmail.com', 
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
