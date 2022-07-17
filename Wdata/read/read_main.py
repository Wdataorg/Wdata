# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

from ..data_py import data


def read_dict(fname: str) -> str:
    return data[fname]['datas']

def read_dict_draw(fname:str) -> list:
    file = data[fname]
    return [file, file['Type']]
