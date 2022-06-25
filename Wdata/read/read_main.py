# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

import json

def read_dict(json_fname: str) -> str:
    with open(f'./Wdata/{json_fname}.json', 'r') as file:
        return json.load(file)['datas']

def read_json(json_fname: str) -> str:
    with open(f'./Wdata/{json_fname}.json' ,'r') as file:
        json_file = json.load(file)
        json_file = json_file['datas']

    return json_file

