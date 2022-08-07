# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: .07.17
Project Name: Wdata
"""

data = {
    'Population_growth':
    {
        "count_unit":"people",
        "Type": "Line Chart",
        "unit": "years",
        "Unit length":10,
        "datas":{
            "1800":900000000,
            "1820":1100000000,
            "1840":1200000000,
            "1860":1300000000,
            "1880":1400000000,
            "1900":1650000000,
            "1920":1800000000,
            "1940":2200000000,
            "1960":3000000000,
            "1980":4400000000,
            "2000":5900000000,
            "2022":7400000000
        }
    },

    'Chinese_spacecraft':{
        "count_unit":"spacecraft",
        "Type": "Line Chart",
        "unit": "years",
        "Unit length":1,
        "datas":{
            "2017": 34,
            "2018": 95,
            "2019": 82,
            "2020.6": 89
        }
    },

    "World_spacecraft":{
        "count_unit":"spacecraft",
        "Type": "Line Chart",
        "unit": "years",
        "Unit length":1,
        "datas":{
            "2017": 467,
            "2018": 438,
            "2019": 492,
            "2020.6": 1277
        }
    }
}

data_list = list(data.keys())