#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Yuri'

from setuptools import setup, find_packages

setup(
    name='selenium-webdriver-manager',
    version='1.0.1',
    description='Simplify management of selenium-drivers for different browsers',
    author='Yuri',
    author_email='yuri_zhong@epam.com',
    platforms=['windows', 'linux', 'macOS'],
    url='https://git.epam.com/yuri_zhong/selenium-webdriver-manager',
    # install_requires=['configparser'],
    packages=find_packages(exclude=['demo']),
    zip_safe=False,
    python_requires='>=3.6'
)

# run 'python setup.py install' in cmd
