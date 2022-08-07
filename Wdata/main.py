# -*- coding:utf-8 -*-


from .data_py import *
from .plot_pic import line_chart
from .read import *
from .all_error import JsonError
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

class Wdata_class():
    def __init__(self, jsonname: str) -> None:
        self.DATA_LIST = data_list
        self.jsonname = jsonname
        if not(self.jsonname in self.DATA_LIST):
            raise JsonError("There is no dataset {}".format(self.jsonname))

    def Fetch_dict(self) -> dict:
        return read_dict(self.jsonname)

    def Save_file(self, filename: str) -> None:
        try:
            with open(f'{filename}.json', 'w+') as file:
                dump(read_dict(self.jsonname), file)
            return True
        except FileNotFoundError:
            raise JsonError('There is no corresponding Json file')

    def __read_json_draw(self) -> dict:
        return read_dict_draw(self.jsonname)

    def draw(self) -> None:
        result = self.__read_json_draw()
        if result[1] == 'Line Chart':
            print('Plot the data for data {}'.format(self.jsonname))
            line_chart(result[0], self.jsonname)
    def __len__(self) -> int:
        return len(self.Fetch_dict())

    def __repr__(self) -> str:
        """
        eg.
        >>> from Wdata import Wdata_class
        >>> test = Wdata_class('Population_growth')
        >>> test
         Wdata_class('Population_growth')
        """
        return 'Wdata_class("{}")'.format(self.jsonname)

    def __getitem__(self, item: int) -> list:
        """
        eg.
        >>> from Wdata import Wdata_class
        >>> test = Wdata_class('Population_growth')
        >>> test[0]
        ("1800", 900000000)
        >>> for year, people in test:
        ...     print("In year:{}, people_growth:{}".format(year, people))
        In year:1800, people_growth:900000000
        In year:1820, people_growth:1100000000
        In year:1840, people_growth:1200000000
        In year:1860, people_growth:1300000000
        In year:1880, people_growth:1400000000
        In year:1900, people_growth:1650000000
        In year:1920, people_growth:1800000000
        In year:1940, people_growth:2200000000
        In year:1960, people_growth:3000000000
        In year:1980, people_growth:4400000000
        In year:2000, people_growth:5900000000
        In year:2022, people_growth:7400000000
        """
        return list(self.Fetch_dict().items())[item]