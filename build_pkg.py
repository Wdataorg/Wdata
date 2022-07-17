# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: .07.17
Project Name: Wdata
"""

from os import system

with open('passwd_uld', 'r+') as file:
    passwd = file.read()

system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python310\python.exe setup.py bdist_egg')
system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python310\python.exe  -m  twine upload  -u __token__ -p {} dist/*'.format(passwd))
system(r'''
        del  /S /Q build;
        del /S /Q dist;
        del /S /Q Wdatabase-1.0.0;
        del /S /Q Wdatabase.egg-info
        ''')
system(r'''
        rmdir build;
        rmdir dist;
        rmdir Wdatabase-1.0.0;
        rmdir Wdatabase.egg-info
        ''')
