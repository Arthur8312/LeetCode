# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 08:53:32 2021

@author: user
"""
"""
解題關鍵: 找到1種rows樣式 在翻轉前與翻轉後最多的rows
因為 統一翻轉後一邊會是0 一邊會是1
"""

import collections
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cache = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            cache[str(vals)] += 1
            cache[str(trans)] += 1

        return max(cache.values())