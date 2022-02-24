#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Filename: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer/definitions.py
Path: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer
Created Date: Saturday, January 29th 2022, 4:14:04 pm
Author: Christian Fink

Copyright (c) 2022 Your Company
"""

import sys
# import time
# import asyncio
# from pathlib import Path

from enum import Enum

class MeasureType(Enum):

    TEMP = 0
    PT100 = 1
    PT1000 = 2
    TE_B = 21
    TE_E = 23
    TE_J = 24
    TE_K = 25
    TE_N = 26
    TE_R = 27
    TE_S = 28
    TE_T = 29
