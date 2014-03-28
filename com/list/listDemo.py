# -*- coding: utf-8 -*-
'''
Created on 2014-3-28

@author: huanghu
'''
#加上index的迭代
def enumerates():
    strings = ['anne', 'beth', 'george', 'damon']
    for index ,string in enumerate(strings):
        print index
        print string
        
#2维列表
def dimensional():
    items = []
    item = ['name' ,'value']
    items.append(item)
    print items

if __name__ == '__main__':
    dimensional()