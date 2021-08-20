# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 16:57:29 2021

@author: user
"""

'''
1. 最簡化為空 root  return0
2. 兩兩項之間的差 為root左右與目前最大值相比
'''

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def count(root ,mx_value):
            if root is None:
                return 0
            mx = max(root.val, mx_value)
            return (root.val >= mx_value) + count(root.right, mx) + count(root.left, mx)
        
        return count(root, root.val)
        