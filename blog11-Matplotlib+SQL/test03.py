# coding=utf-8
'''
' 这篇代码主要讲述获取MySQL中数据，再进行简单的统计
' 统计采用SQL语句进行 By：Eastmount
'''
 
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import pylab
import MySQLdb
from pylab import *
from pandas import *
 
 
# 根据SQL语句输出24小时的柱状图
try:
    conn = MySQLdb.connect(host='localhost',user='root',
                         passwd='123456',port=3306, db='test01')
    cur = conn.cursor() #数据库游标
 
    #防止报错:UnicodeEncodeError: 'latin-1' codec can't encode character
    conn.set_character_set('utf8')
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    sql = '''select DATE_FORMAT(FBTime,'%Y'), Count(*) from csdn
                group by DATE_FORMAT(FBTime,'%Y');'''
    cur.execute(sql)
    result = cur.fetchall()        #获取结果复合纸给result
    day1 = [n[0] for n in result]
    print len(day1)
    num1 = [n[1] for n in result]
    print len(num1),type(num1)
    matplotlib.style.use('ggplot')
    df=DataFrame(num1, index=day1,columns=['Nums'])
    plt.show(df.plot(kind='bar'))
    plt.savefig('05csdn.png',dpi=400)
 
 
#异常处理
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()  
    conn.close()
 
    