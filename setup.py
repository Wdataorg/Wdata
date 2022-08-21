# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

from setuptools import setup
from Wdata.version import __VERSION__

def read(filename: str) -> str:
    with open(filename, 'r+', encoding='utf-8') as file:
        return file.read()

NAME = "Wdatabase"
VERSION = __VERSION__
AUTHOR = 'Wdataorg'
AUTHOR_EMAIL = "rainwang_20220102@163.com"
MAINTAINER = 'Wdataorg'
MAINTAINER_EMAIL = "rainwang_20220102@163.com"
URL = "https://github.com/Wdataorg/Wdata"
DESCRIPTION = 'A database with multiple data sets that support drawing, These data sets are: World population data set, World Carbon dioxide Concentration data set, World Number of Cities data set, China number of population data set, China number of space vehicles data set......'
LONG_DESCRIPTION = '\n'.join([DESCRIPTION, read('README.md')])
REQUIREMENTS = ['setuptools~=62.3.4',
                'matplotlib~=3.5.2',
                'openpyxl~=3.0.10',
                'simplejson~=3.17.6'
                ]
PACKAGES = ["Wdata", 'Wdata.read', 'Wdata.all_error', 'Wdata.plot_pic']
python_requires = '>=3.8'
LICENSE = read('LICENSE')

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
            'Environment :: Console',
            'Natural Language :: Chinese (Simplified)',
            'Natural Language :: English',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'Development Status :: 5 - Production/Stable',
            'Topic :: Database :: Database Engines/Servers',
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
            'Operating System :: OS Independent'
        ],
    python_requires=python_requires,
    license=LICENSE
)