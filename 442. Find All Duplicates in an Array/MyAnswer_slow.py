# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:31:54 2021

@author: user
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s1 = set()
        s2 = set()
        for i in nums:
            if i not in s1:
                s1.add(i)
            else:
                s2.add(i)
        return list(s2)