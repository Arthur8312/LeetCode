# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 13:59:40 2021

@author: arthur
"""

import collections

multi_dict = collections.defaultdict(list) #不需要判斷key是否於dict中


key_values = [('even',2),('odd',1),('even',8),('odd',3),('float',2.4),('odd',7),('even',4)]

for key,value in key_values:
    multi_dict[key].append(value)