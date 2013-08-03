'''
Created on 2013-4-3

@author: huanghu
'''

class Base(object):
    def __init__(self):
        '''
        Constructor
        '''
        print "base"
        
    def do(self):
        print "base do something"
        
class Son1(Base):
    def __init__(self):
        print "son1"
        
    def doSon1(self):
        print "son1 do something"
        
if __name__ == "__main__":
    son1 = Son1();
    son1.do()