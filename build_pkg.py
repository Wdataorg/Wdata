# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: .07.17
Project Name: Wdata
"""

from os import system

with open(r'D:\password\passwd_uld', 'r+') as file:
    passwd = file.read()

gen_list = [ 'bdist', 'bdist_egg', 'bdist_wheel']

system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python38-32\python.exe setup.py sdist')
for gen_type in gen_list:
    system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python310\python.exe setup.py {}'.format(gen_type))
    system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python38-32\python.exe setup.py {}'.format(gen_type))
    system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python39\python.exe setup.py {}'.format(gen_type))

