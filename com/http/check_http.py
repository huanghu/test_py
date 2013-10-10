# _*_ coding:utf-8 _*_
'''
Created on 2013-4-3

@author: huanghu
通过url判断是否存在此连接
'''
import httplib, urlparse

def httpExists(url):
    host ,path = urlparse.urlsplit(url)[1:3]
    if ':' in host:
        
        host ,port = host.split(':' ,1)
        try:
            port = int(port)
        except ValueError:
            print 'invalid port number %r' % (port ,)
            return False
        
    try:
        connection = httplib.HTTPConnection(host ,port=port)
        connection.request("GET" ,path);
        resp = connection.getresponse();
        print str(resp.status) + " " + resp.reason

        data1 = resp.read()
        print "data " , data1
        found = True;
    except Exception ,e:
        print e.__class__, e, url
        found = False
    return found

if __name__ == '__main__':
    url = raw_input("输入url:")
    httpExists(url);