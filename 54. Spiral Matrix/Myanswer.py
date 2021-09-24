# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:28:18 2021

@author: user
"""


from collections import deque
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        status = 1
        d = deque(matrix)

        temp = []
        while d and d[0]:
            if status == 1:
                temp.extend(d.popleft())
                status = 2
            elif status == 2:
                for i in range(len(d)):
                    temp.append(d[i].pop())
                status = 3
            elif status == 3:
                temp.extend(d.pop()[::-1])
                status = 4
            elif status == 4:
                for i in range(len(d)-1,-1,-1):
                    temp.append(d[i].pop(0))
                status = 1
                
        return temp