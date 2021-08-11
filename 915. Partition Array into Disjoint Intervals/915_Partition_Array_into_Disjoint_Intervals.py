# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 07:54:48 2021

@author: user
"""

class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        disjoint = 0
        leftmax = curmax = nums[0]
        for i,num in enumerate(nums):
            curmax = max(curmax, num)
            if num < leftmax:
                leftmax = curmax
                disjoint = i
        return disjoint + 1 