# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

from setuptools import setup
from Wdata.version import  __VERSION__

def read(filename: str) -> str:
    with open(filename, 'r+') as file:
        return file.read()

NAME = "Wdata"
VERSION = __VERSION__
AUTHOR = 'Wdataorg'
AUTHOR_EMAIL = "rainwang_20220102@163.com"
MAINTAINER = 'Wdataorg'
MAINTAINER_EMAIL = "rainwang_20220102@163.com"
URL = "https://https://github.com/Wdataorg/Wdata"
DESCRIPTION = 'A database with multiple data sets that support drawing, These data sets are: World population data set, World Carbon dioxide Concentration data set, World Number of Cities data set, China number of population data set, China number of space vehicles data set......'
LONG_DESCRIPTION = '\n'.join([DESCRIPTION, read('README.md')])
REQUIREMENTS = ['setuptools~=62.3.4']
PACKAGES = ['Wdata', 'Wdata.json', 'Wdata.read', 'Wdata.Error']
python_requires = '>=3.6'

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url=URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=REQUIREMENTS,
    packages=PACKAGES,
    long_description_content_type='text/markdown',
    project_urls={
            'Documentation': 'https://github.com/Wdataorg/Wdata#readme',
            'Source': 'https://github.com/Wdataorg/Wdata',
            'Tracker': 'https://github.com/Wdataorg/Wdata/issues',
            'Funding': 'https://wdataorg.github.io/Sponsor/',
        },
    classifiers=[
            'Topic :: Data',
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: Implementation',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'License :: Apache License 2.0',
            'Operating System :: OS Independent',
        ],
    python_requires=python_requires
)
