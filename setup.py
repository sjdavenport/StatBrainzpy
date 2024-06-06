from distutils import sysconfig
from setuptools import setup, Extension, find_packages
import os
import sys
import setuptools
from copy import deepcopy

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyperm',
    install_requires=[
        'numpy',
        'ants',
        'matplotlib'
    ],
    version='0.0.1',
    license='MIT',
    author='Samuel DAVENPORT',
    download_url='https://github.com/sjdavenport/StatBrainzpy/',
    author_email='sdavenport@health.ucsd.edu',
    url='https://github.com/sjdavenport/StatBrainzpy/',
    long_description=long_description,
    description='Python Toolbox of Functions for performing statistical inference for neuroimaging data',
    keywords='Permutation, Bootstrap, fMRI, Post-hoc inference',
    packages=find_packages(),
    python_requires='>=3',
)
