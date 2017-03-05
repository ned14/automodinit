#!/usr/bin/env python
# automodinit
# Solves the problem of forgetting to keep __init__.py files up to date
# (C) 2012 Niall Douglas http://www.nedproductions.biz/
# See http://pypi.python.org/pypi/automodinit for latest version
# Go to http://github.com/ned14/automodinit to report bugs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'Readme.txt')) as f:
    long_description = f.read()
    
setup(
    name='automodinit',
    version="0.16",
    description='Solves the problem of forgetting to keep __init__.py files up to date',
    long_description=long_description,
    author='Niall Douglas',
    url='http://pypi.python.org/pypi/automodinit',
    packages=["automodinit", ],
    test_suite='tests',
    install_requires=[],
    package_data={'':['Readme.txt']},
    license='MIT',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    )
