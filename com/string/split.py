# -*- coding: utf-8 -*-
'''
Created on 2014-3-28

@author: huanghu
'''

def splitDemo():
    s = '#sfsdfd'
    print s.split('#')[1]
    print len(s.split('#'))
    print len(s.split('='))
    #s.split('=')[-1] 如果只有一个等号，可以写-1

if __name__ == '__main__':
    splitDemo()