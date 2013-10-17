# -*- coding: utf-8 -*-
'''
Created on 2013-10-14

@author: huanghu
'''
#property函数实例
class Property(object):
    
    def getSize(self):
        return self.size
        
    def setSize(self ,size):
        self.size = size
        
if __name__ == '__main__':
    pro = Property()
    pro.setSize(1)
    print pro.getSize()