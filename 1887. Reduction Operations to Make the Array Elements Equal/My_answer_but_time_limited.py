# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:43:22 2021

@author: user
"""
#my answer but time limited
#用set計算 最大值*set的長度
#推測nums.counts緣故
class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = sorted(set(nums), reverse = True)
        set_len = len(nums_set)
        cnt = 0
        for i, num in enumerate(nums_set):
            cnt = cnt + (set_len-i-1)*nums.count(num)
        
        return cnt