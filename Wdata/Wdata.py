# -*- coding:utf-8 -*-

from read.read import (read_json, read_dict)
from error.Error import JsonError

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

class Wdata(object):
    """
    Wdata:
        Author: Wdataorg,
        Author_Email = rainwang_20220102@163.com,

        Function:
            ----------------------------------------------------------------------------------------------------------------------------------------------
            Name                Result_Type         Description                                                                         parameter               status
            Fetch_dict          dict                Get the dictionary corresponding to the json dataset                                None                    In maintenance
            Save_file           bool                Store the json dataset in a json file and return a boolean value of success         filename                In maintenance

        init_parameter:
            ---------------------------------------------------------------------
            Name            Description
            jsonname        Json dataset name

    """

    def __init__(self, jsonname: str):
        self.jsonname = jsonname
        try:
            with open(f'../json/{self.jsonname}.json'):
                pass
        except FileNotFoundError:
            raise JsonError

    def Fetch_dict(self):
        return read_dict(self.jsonname)

    def Save_file(self, filename: str):
        try:
            with open(f'{filename}.json') as file:
                file.write(read_json(self.jsonname))
            return True
        except FileNotFoundError:
            return False

