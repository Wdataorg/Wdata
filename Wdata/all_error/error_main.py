# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

class JsonError(Exception):
    def __init__(self, message):
        super().__init__(message)