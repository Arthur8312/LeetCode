# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:40:09 2021

@author: user
"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        o = nums.index(max(nums))
        max_num = max(nums)
        nums.pop(o)
        if len(nums)==0 or max_num >= 2*max(nums):
            return o
        else:
            return -1