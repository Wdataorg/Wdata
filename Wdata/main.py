# -*- coding:utf-8 -*-

from .data_py import data_list
from .plot import line_chart
from .read import *
from .error import JsonError
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

DATA_LIST = data_list

class Wdata_class(object):
    def __init__(self, jsonname: str):
        self.jsonname = jsonname
        if not(self.jsonname in DATA_LIST):
            raise JsonError("There is no dataset {}".format(self.jsonname))

    def Fetch_dict(self):
        try:
            return read_dict(self.jsonname)
        except Exception as ex:
            raise JsonError(ex)
        return read_dict(self.jsonname)

    def Save_file(self, filename: str):
        try:
            with open(f'{filename}.json', 'w+') as file:
                dump(read_dict(self.jsonname), file)
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
