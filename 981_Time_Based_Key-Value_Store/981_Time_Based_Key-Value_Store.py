# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 12:37:07 2021

@author: arthur
"""
## set會重小到大排列 所以不用特地sort
## 使用binary search 速度才夠

import collections
class TimeMap(object):

    def __init__(self):
        self.dic = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dic[key]
        n = len(arr)
        
        left = 0
        right = n
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid
        
        return "" if right == 0 else arr[right - 1][1]
    
if __name__ == '__main__':
    
#    A1 = ["TimeMap","set","set","get","get","get","get","get"]
#    A2 = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    A1 = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    A2 = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    out = []
    for i in range(len(A1)):
        if A1[i] == "TimeMap":
            timestep = TimeMap()
            out.append('null')
        elif A1[i] == "set":
            timestep.set(A2[i][0], A2[i][1], A2[i][2])
            out.append('null')
        elif A1[i] == "get":
            out.append(timestep.get(A2[i][0], A2[i][1]))
    
    