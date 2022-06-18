# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

import json

def read_dict(json_fname: str) -> str:
    with open(f'../json/{json_fname}.json') as file:
        json_file = file.read()

    return json.loads(json_file)['datas']

def read_json(json_fname: str) -> str:
    with open(f'../json/{json_fname}') as file:
        json_file = json.loads(file.read())
        json_file = json_file['data']

    return json_file

