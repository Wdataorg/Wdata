# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: .08.21
Project Name: Wdata
"""
from os import system

with open(r'D:\password\passwd_uld', 'r+') as file:
    passwd = file.read()

system(r'C:\Users\S.X.Y\AppData\Local\Programs\Python\Python310\python.exe  -m  twine upload  -u __token__ -p {} dist/*'.format(passwd))

folder_list = ['build', 'dist', ' Wdatabase.egg-info']

for i in folder_list:
    system('rmdir -f {}'.format(i))