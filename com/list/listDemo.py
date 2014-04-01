# -*- coding: utf-8 -*-
'''
Created on 2014-3-28

@author: huanghu
'''
#加上index的迭代
def enumerates():
    strings = ['anne', 'beth', 'george', 'damon']
    for index ,string in enumerate(strings):
        print index
        print string
        
#2维列表
def dimensional():
    items = []
    item = ['queryName', 'queryName22']
    items.append(item)
    print items
    
#
def count():
    item = ['name' ,'value']
    c = item.count('name')
    print c

#遍历2维列表
def foreachDimensional():
    items = [['nameNode', 'hdfs://hadoop-master.360buy.com:8020'], ['jobTracker', 'hadoop-master.360buy.com:8021'], ['queueName', 'erpmerge'], ['emailList', 'huanghu@jd.com'], ['executeMode', '0'], ['system', 'main/product/ebook/mtlSystemItemsEbook_U'], ['dbName', 'ebook'], ['dbName2', 'forest'], ['queryName', 'mtlSystemItemsEbook'], ['queryName_sort', 'ebookSort'], ['srcSystem', 'EBOOK'], ['groupName', 'JD_MTL_SYSTEM_ITEMS_I'], ['tableName', 'JD_MTL_SYSTEM_ITEMS_I'], ['getLatestOperationTime', 'SELECT MAX(modified) FROM ebook'], ['\n', ''], ['commonPath', '${nameNode}/user/${user.name}/oozie/workflow/common'], ['wf_app_path', '${nameNode}/user/${user.name}/oozie/workflow/${system}'], ['mapping_path', '${wf_app_path}/ebook-mapping.xml'], ['import_path', '${wf_app_path}/importData.xml'], ['\n', ''], ['checkLockSequence', '1'], ['waitingThreshold', '5'], ['failThreshold', '9'], ['nolockTime', '30'], ['frequency', '5760'], ['\n', ''], ['oozie.libpath', '/user/${user.name}/share/lib'], ['oozie.wf.application.path', '${wf_app_path}'], ['\n', ''], ['\n', ''], ['start', '2013-05-30T02:00Z'], ['end', '2013-06-10T06:00Z'], ['\n', ''], ['actionType', 'UPDATE']]
    for item in items:
        #遍历的过程中不能remove
        items.remove(item)
        print item

if __name__ == '__main__':
    foreachDimensional()