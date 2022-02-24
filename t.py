#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Filename: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer/t.py
Path: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer
Created Date: Tuesday, February 22nd 2022, 9:15:25 pm
Author: Christian Fink

Copyright (c) 2022 Your Company
"""

import sys
# import time
# import asyncio
# from pathlib import Path
import pandas as pd

if __name__ == "__main__":
    

    d = {
        'Bezeichnung': [
            'label',
            'id',
            'CL'
        ],
        'Wert': [
            'Dies ist das Label',
            12345,
            "SCS-2022-02-22"
        ]
    }

    print(d)

    # df = pd.DataFrame.from_dict(d, orient='index', columns=['Bezeichnung', 'Wert'])
    df = pd.DataFrame.from_dict(d)
    print(df)
