# -*- coding:utf-8 -*-
"""
Author: Wdataorg
Date: .11.12
Project Name: Wdata
"""

import math

def similarity(xy1: tuple, xy2: tuple) -> float:
    """
    This function can use the cosine similarity formula to calculate the similarity of the two coordinates and return
    the similarity value

    :param xy1: tuple
    :param xy2: tuple
    :return: float
    """
    result = (xy1[0] * xy2[0] + xy1[1] * xy2[1]) / ((math.sqrt(xy1[0] ** 2 + xy1[1] ** 2)) * (math.sqrt(xy2[0] ** 2 + xy2[1] ** 2)))
    return result

def distance(xy1: tuple, xy2: tuple) -> float:
    """
    This function can use Euclid distance formula to calculate the distance of 2 coordinates and return
     the distance value

    :param xy1: tuple
    :param xy2: tuple
    :return: float
    """
    result = math.sqrt((xy1[0] - xy2[0])**2 + (xy1[1]-xy2[1])**2)
    return result