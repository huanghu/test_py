'''
Created on 2014-3-28

@author: huanghu
'''

def items():
    d = dict();
    d['name'] = 'jd'
    
    item = d.items();
    print item[0][0];
    print item[0][1];

if __name__ == '__main__':
    items()