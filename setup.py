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

setup(
    name='automodinit',
    version="0.13",
    description='Solves the problem of forgetting to keep __init__.py files up to date',
    author='Niall Douglas',
    url='http://pypi.python.org/pypi/automodinit',
    packages=["automodinit", ],
    test_suite='tests',
    install_requires=[],
    )
