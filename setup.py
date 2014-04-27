# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import trampoline
version = trampoline.__version__

setup(
    name='trampoline',
    version=version,
    author='',
    author_email='agam@comfylabs.io',
    packages=[
        'trampoline',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['trampoline/manage.py'],
)