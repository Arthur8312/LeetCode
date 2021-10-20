# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:32:51 2021

@author: user
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []
        for i in nums1:
            temp = nums2[nums2.index(i):len(nums2)]
            print(temp)
            c = -1
            for j in temp:
                if j > i:
                    c = j   
                    break
            out.append(c)
        return out