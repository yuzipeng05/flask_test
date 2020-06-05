# coding=utf-8
# @Auther : "鹏哥贼优秀"
# @Date : 2019/9/23
# @Software : PyCharm

from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)
con = sqlite3.connect('material.db', check_same_thread=False)

@app.route('/')
def Material_Mangement():
    # 获取数据库material_table表的内容
    cur = con.cursor()
    sql = 'select * from {0}'.format("material_table")
    cur.execute(sql)
    content = cur.fetchall()
    # 获取数据库表的表头
    labels = [tuple[0] for tuple in cur.description]
    return render_template('test.html', content=content, labels=labels)



@app.route('/delete')
def ck_test():
    ip_str = request.args.get("ip")
    ip_list = eval(ip_str)
    print(ip_list)
    for ip in ip_list:
        if ip:
            sql = "delete from material_table where 网络IP='{}'".format(ip)
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
    return "删除数据成功！"


@app.route('/edit', methods=['get'])
def edit():
    label = ['ID', '网络IP', '地址', '责任人', '联系方式']
    content = [request.args.get(i) for i in label]
    print(content)
    sql = 'update {0} set {1}="{6}",{2}="{7}",{3}="{8}",{4}="{9}" where {5}={10}'.format('material_table',
          label[1], label[2], label[3],label[4],label[0],content[1],content[2],content[3],content[4],content[0])
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return "数据写入成功！"

if __name__ == '__main__':
    app.run(host="11.240.65.176",debug=True)