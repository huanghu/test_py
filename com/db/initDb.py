'''
Created on 2013-8-5

@author: huanghu
'''
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(host='192.168.232.64' ,user='test' ,passwd='123456' ,db='oozie')
    cursor = connection.cursor();
    count = cursor.execute("select * from coord_actions limit 1");
    print "count " + str(count)
    
    result = cursor.fetchone();
    print result;
    