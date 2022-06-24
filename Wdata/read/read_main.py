# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

import json

def read_dict(json_fname: str) -> str:
    with open(f'./{json_fname}.json', mode="w+") as file:
        return json.load(file)

def read_json(json_fname: str) -> str:
    with open(f'./{json_fname}.json') as file:
        json_file = json.load(file)
        json_file = json_file['datas']

    return json_file

