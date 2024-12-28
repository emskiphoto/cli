#!/usr/bin/env python

from setuptools import setup

if __name__ == "__main__":
    setup(name = 'cli',
    version = '0.1.0',
    packages = ['cli'],
    entry_points = {
        'console_scripts': [
            'cli = cli.main:main'
        ]
    })