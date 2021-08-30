# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:17:26 2021

@author: arthur
"""
#解題關鍵 Backtracking



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stack = [[]]
        for i in nums:
            new_stack = []
            
            for j in stack:
                print('j:{}'.format(j))
                new_stack.append(j) 
                if j:
                    new_stack.append(j + [i])
                else:
                    new_stack.append([i])
            stack = new_stack
            
            
        return stack