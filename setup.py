#!/usr/bin/env python
# automodinit
# Solves the problem of forgetting to keep __init__.py files up to date
# (C) 2012 Niall Douglas http://www.nedproductions.biz/
# See http://pypi.python.org/pypi/automodinit for latest version
# Go to http://github.com/ned14/automodinit to report bugs

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name='automodinit',
    version="0.12",
    description='Solves the problem of forgetting to keep __init__.py files up to date',
    author='Niall Douglas',
    url='http://pypi.python.org/pypi/automodinit',
    packages=find_packages(),
    test_suite='tests',
    install_requires=[],
    )
