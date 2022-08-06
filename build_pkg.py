# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: .07.17
Project Name: Wdata
"""

from os import system

with open('passwd_uld', 'r+') as file:
    passwd = file.read()

gen_list = ['sdist', 'bdist', 'bdist_egg', 'bdist_rpm']

for gen_type in gen_list:
    system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python310\python.exe setup.py {}'.format(gen_type))
    system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python38-32\python.exe setup.py {}'.format(gen_type))

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
