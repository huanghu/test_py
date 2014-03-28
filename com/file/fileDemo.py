# -*- coding: utf-8 -*-
'''
Created on 2013-10-15

@author: huanghu
'''

def read():
    path = "test.txt";
    files = open(path, "r");
    contents = files.readlines()
#    for content in contents:
#        print content;
    return contents
        
def constructDict():
    contents = read()
    d = dict()
    
    for content in contents:
        index = content.index('=')
        content = content[index:len(content)].decode('utf-8');
        d[content[0:index]] = content
    print d;

if __name__ == '__main__':
    constructDict();