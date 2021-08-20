# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:09:53 2021

@author: user
"""
#key 1 將中間當作大迴圈
#key 2 用相乘計算
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        c = 0
        for i, value in enumerate(rating):
            AB_c = BC_c = BA_c = CB_c = 0
            for j in rating[:i]: 
                if value > j:
                    BA_c += 1
                if j > value:
                    AB_c += 1
            for j in rating[i:]: 
                if value > j:
                    BC_c += 1
                if j > value:
                    CB_c += 1
            c += AB_c*BC_c + BA_c*CB_c
        return c