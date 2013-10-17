'''
Created on 2013-10-16

@author: huanghu
'''

#utf-8转换为gbk
def transCode():
    s = '输入svn版本号：'
    print s.decode('utf-8').encode('gbk')

if __name__ == '__main__':
    transCode()