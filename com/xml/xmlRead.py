# -*- coding: utf-8 -*-
'''
Created on 2013-10-8

@author: huanghu
'''

from xml.dom import minidom


def read():
    doc = minidom.parse('workflow.xml')
    root = doc.documentElement
    #获得根节点的attributes,其他
    print root.attributes.get('name').nodeValue
    pass

if __name__ == '__main__':
    read()
    pass