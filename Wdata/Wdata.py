# -*- coding:utf-8 -*-

from json import dump
import read
from Error import JsonError

"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

"""
A database with multiple data sets that support drawing, 
These data sets are:
World population data set, World Carbon dioxide Concentration data set, 
World Number of Cities data set,
China number of population data set, 
China number of space vehicles data set......
"""

class Wdata():
    def __init__(self, jsonname: str):
        self.jsonname = jsonname

    def Fetch_dict(self):
        try:
            return read.read_dict(self.jsonname)
        except Exception as ex:
            raise JsonError(ex)

    def Save_file(self, filename: str):
        try:
            with open(f'{filename}.json') as file:
                dump(read.read_json(self.jsonname))
            return True
        except FileNotFoundError:
            raise JsonError('There is no corresponding Json file')

# for assets

test = Wdata("Population_growth")
print(test.Fetch_dict())