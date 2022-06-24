# -*- coding:utf-8 -*-

import Wdata.read
from Wdata.Error import JsonError
from json import dump

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

class Wdata_class(object):
    def __init__(self, jsonname: str):
        self.jsonname = jsonname

    def Fetch_dict(self):
        return Wdata.read.read_dict(self.jsonname)

    def Save_file(self, filename: str):
        try:
            with open(f'{filename}.json') as file:
                dump(Wdata.read.read_json(self.jsonname))
            return True
        except FileNotFoundError:
            return False

