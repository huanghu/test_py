# -*- coding: utf-8 -*-
'''
Created on 2014-3-14

@author: huanghu
'''
from xml.dom import minidom

def write():
    impl = minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'employees', None)
    root = dom.documentElement  
    employee = dom.createElement('employee')
    root.appendChild(employee)
  
    nameE=dom.createElement('name')
    nameT=dom.createTextNode('linux')
    nameE.appendChild(nameT)
    employee.appendChild(nameE)
  
    ageE=dom.createElement('age')
    ageT=dom.createTextNode('30')
    ageE.appendChild(ageT)
    employee.appendChild(ageE)
  
    f= open('employees2.xml', 'w')
    dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
    f.close()
    
if __name__ == '__main__':
    write()
    