# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 10:06:50 2021

@author: arthur
"""
##判斷每個元素是否 有兩個以上街角
##Falie 沒辦法判斷是否封閉
import numpy as np
def search_set(elm, elm_list):
    cnt = 0
    nerbys = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for nerby in nerbys:
        setSearchKey = elm + nerby
        if setSearchKey.tolist() in elm_list.tolist():
            cnt = cnt+1
    if cnt >= 2:
        return 0
    return 1
def containsCycle(grid):
    a = np.array(grid)
    c = np.array(grid)
    c = np.reshape(c, (-1))  
    unique = []
    for i in c:
        if i not in unique:
            unique.append(i)
            elm_list = np.argwhere(a == i)
            if len(elm_list) >= 4:
                j = 0
                for elm in elm_list:        
                    if search_set(elm, elm_list):                        
                        elm_list = np.delete(elm_list, j, axis=0)
                        j = j-1
                    if len(elm_list) < 4:
                        break
                    j = j+1
                else:
                    return 1
    return 0

if __name__ == '__main__':
    grid = [["d","f","d","b","b","d","f","c","e"],
            ["f","c","e","d","c","f","b","d","c"],
            ["f","f","e","e","d","a","f","b","c"],
            ["b","b","a","a","c","e","c","c","c"],
            ["e","d","d","b","f","c","c","f","a"],
            ["c","a","e","a","b","a","b","f","f"],
            ["c","d","a","d","d","b","e","b","c"],
            ["b","b","e","a","c","e","a","c","e"],
            ["f","e","d","e","b","c","b","f","c"],
            ["f","c","c","c","e","a","c","f","d"],
            ["a","c","a","c","a","f","d","f","d"],
            ["b","f","e","c","c","a","a","e","b"],
            ["f","a","c","e","f","d","f","f","e"],
            ["d","e","c","a","d","f","c","c","b"]]
#    a = np.array(grid)
#    elm_list = np.argwhere(a == 'a')
#    for i ,elm in enumerate(elm_list):
#        print(i, elm)
#    t = np.delete(elm_list, 0, axis=0)
#    a = np.array(grid)
#    elm_list = np.argwhere(a == 'c')
#    print(search_set([0,0], elm_list))
#    elm = [1, 1]
    


        
##        
    print(containsCycle(grid))
##    containsCycle(grid)