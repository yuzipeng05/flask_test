# coding=utf-8
# @Auther : "鹏哥贼优秀"
# @Date : 2019/9/23
# @Software : PyCharm

import sqlite3

tablename = "material_table"
con = sqlite3.connect('material.db')
cur = con.cursor()
label = ['ID','网络IP','地址','责任人','联系方式']
content = ['1','10.10.10.10','杭州滨江','鹏哥','123456']

def create():
    sql = 'create table {0} ({1},{2},{3},{4},{5})'.format(tablename,label[0],label[1],label[2],label[3],label[4])
    result = cur.execute(sql)
    con.commit()
    return  True if result else False

def insert():
    sql = 'insert into {0} ({1},{2},{3},{4},{5}) values({6},"{7}","{8}","{9}","{10}")'.format(tablename,label[0],label[1],
          label[2],label[3],label[4],content[0],content[1],content[2],content[3],content[4])
    result = cur.execute(sql)
    con.commit()
    return  True if result else False

def query():
    sql = 'select * from {0}'.format(tablename)
    result = cur.execute(sql)
    return list(result)

print("数据表创建结果:",create())
print("数据表插入数据结果:",insert())
print("数据表查询结果:",query())


