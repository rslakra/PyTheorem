#
# Author: Rohtash Lakra
#
from setuptools import setup, find_packages

setup(
    name='pycli',
    version='0.1.0',
    description='PyTheorem: A Python Learning & Data Structures',
    url='https://github.com/rslakra/PyTheorem',
    author='Rohtash Lakra',
    author_email='work.lakrak@gmail.com',
    license='MIT',
    install_requires=['requests'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=[
            'pycli = pycli.main:main',
        ]
    ))
