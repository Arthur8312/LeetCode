# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:18:07 2021

@author: user
"""
#28 ms, faster than 97.78% 

class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        Temp = range(1, m+1)

        out = []
        for i in queries:
            p = Temp.index(i)
            out.append(p)
            item = Temp.pop(p)
            Temp.insert(0, item)

        return out