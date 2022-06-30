# -*- coding:utf-8 -*-

from plot import line_chart
from read import *
from error import JsonError
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
        try:
            return read_dict(self.jsonname)
        except Exception as ex:
            raise JsonError(ex)
        return Wdata.read.read_dict(self.jsonname)

    def Save_file(self, filename: str):
        try:
            with open(f'{filename}.json') as file:
                dump(read_json(self.jsonname))
            return True
        except FileNotFoundError:
            raise JsonError('There is no corresponding Json file')
    def __read_json_draw(self):
        return read_dict_draw(self.jsonname)

    def draw(self):
        result = self.__read_json_draw()
        if result[1] == 'Line Chart':
            print('Plot the data for data {}'.format(self.jsonname))
            line_chart(result[0], self.jsonname)
# for assets

test = Wdata_class('Population_growth')
test.draw()