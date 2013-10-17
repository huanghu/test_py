# -*- coding:utf-8 -*-
'''
Created on 2013-10-14

@author: huanghu
'''

#去掉空格，回车
def delEntry():
    s = "test space\r\n"
    print s.split()
    print ''.join(s.split())

if __name__ == '__main__':
    delEntry()