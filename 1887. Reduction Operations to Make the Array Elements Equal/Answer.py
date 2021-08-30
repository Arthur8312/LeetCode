# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:52:18 2021

@author: user
"""
#討論區的解答
#利用index做累加
class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort(reverse=True)
        smallest = nums[0]
        for index, num in enumerate(nums):
            if smallest > num:
                smallest = num
                result += index
        
        return result