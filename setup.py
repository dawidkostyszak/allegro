#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='allegro',
    version='0.1',
    description='Coroutine-based networking library',
    author='Dawid Kostyszak',
    author_email='dawid.kostyszak@stxnext.pl',
    url='http://stxnext.pl',
    packages=['lib'],
    install_requires = [
        'mechanize',
        'beautifulsoup4',
        'mock',
    ],
    entry_points={
          'console_scripts': [
              'allegro = lib.scripts:parser']
              }
)
