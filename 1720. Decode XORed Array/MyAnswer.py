# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:50:22 2021

@author: user
"""
# AXorB =C CXorB =A

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        out = [first]
        temp = first
        for i in encoded:
            temp = temp ^ i
            out.append(temp)
        return out