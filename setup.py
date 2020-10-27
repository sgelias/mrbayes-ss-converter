#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
from setuptools import setup, find_packages

try:
    from setuptools import setup
    from setuptools import Command
    from setuptools import Extension
except ImportError:
    sys.exit(
        "We need the Python library setuptools to be installed. "
        "Try runnning: python -m ensurepip"
    )


REQUIRES = []


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup_args = dict(

    # About package
    name = 'MrBayeStruConverter',
    version = '0.0.2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['MrBayes', 'Phylogeny', 'Ribosome'],
    url = 'https://github.com/sgelias/mrbayes-ss-converter.git',
    packages = find_packages(),
    package_dir={'MrBayeStruConverter': 'MrBayeStruConverter'},

    # About author
    author = "Samuel Galvão Elias",
    author_email = 'sgelias@outlook.com',

    # Language and Licence
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)


if __name__ == '__main__':
    setup(install_requires=REQUIRES, **setup_args)
