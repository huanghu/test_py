# _*_ coding:utf-8 _*_
'''
Created on 2013-4-3

@author: huanghu
'''
from base import Base,Son1


class Son(Son1):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        print "son"
        
    def doSon(self):
        print "son do something"
        
if __name__ == "__main__":
    son1 = Son1();
    son1.do()
    
    son = Son();
    #继承只有当两个类在一个文件下才有效