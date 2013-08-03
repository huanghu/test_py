#__*__ coding:utf-8 __*__
'''
Created on 2013-4-3

@author: huanghu
'''

def formatStr():
    value = " %s %s=%s %s" % ("1" ,"2" ,"3" ,"4")
    print value
    
def unicode2Utf():
    #unicode转换为utf8
    string = u'\u63a5\u53e3ID';
    print '测试 ' + string.decode()
    

if __name__ == '__main__':
    #unicode转换为utf8
    string = u'\u63a5\u53e3ID';
    print '测试 ' + string
