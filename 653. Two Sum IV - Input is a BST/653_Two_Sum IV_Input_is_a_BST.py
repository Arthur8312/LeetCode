# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:04:36 2021

@author: user
"""

#重點1: 兩個elemet相加 反向思考利用剪髮
#重點2: set()不會加入重複的元素

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack, seen = [root], set()
        
        while stack:
            curr = stack.pop()
            # If we've seen k - curr.val,
            # we have k - curr.val + curr.val = k
            if k - curr.val in seen:
                return True
            seen.add(curr.val)

            # Visit children
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        return False