# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: 2022.06.17
Project Name: Wdata
"""

class JsonError(Exception):
    """
    The error is triggered when:
        1. The dataset entered by the user does not exist
    """
    def __init__(self, message):
        super().__init__(message)

class FileTypeError(Exception):
    """
    The error is triggered when:
        1. The file format entered by the user does not exist
    """
    def __init__(self):
        def __init__(self, message):
            super().__init__(mesage)