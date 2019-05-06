# -*- coding: utf-8 -*-
import pypyodbc
from sales import *
import pickle
import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import datetime
import numpy as np
import math
# matplotlib inline
plt.style.use('ggplot')

def read_data():
    pypyodbc.lowercase = False
    conn = pypyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
        r"Dbq=C:\Users\Vicon\PycharmProjects\DatabaseAccess\AllSales.accdb;")
    cur = conn.cursor()
    cur.execute("SELECT * FROM AllSales where customerid<>'<null>' and createtime>='20180101' and createtime<'20190101' and 订单类型<>'退货' Order by btd asc") #where customerid<>'<null>' and createtime>='20180101' and createtime<'20190101'
    orders = list()
    while True:
        row = cur.fetchone()
        if row is None:
            break
        tmp = list()
        for item in row:
            tmp.append(item)
        orders.append(tmp)

    orderFrame = DataFrame(orders)
    orderFrame.rename(
        columns={0: 'part', 1: 'storeid', 2: 'storename', 3: 'customerid', 4: 'customername', 5: 'birthday',
                 6: 'tier', 7: 'club', 8: 'salesorder', 9: 'createtime', 10: 'salestype', 11: 'sku',
                 12: 'skuname', 13: 'itemtype', 14: 'marketprice', 15: 'revenue', 16: 'quantity', 17: 'fst',
                 18: 'fststore', 19: 'fstrevenue', 20: 'lst', 21: 'bcid', 22: 'bcname'}, inplace=True)
    # orderFrame['birthday'] = orderFrame['birthday'].where(orderFrame['birthday']!=None, other='<null>', inplace=True)
    # print(orderFrame['birthday'])
    fw = open('orderObj.txt','wb')
    pickle.dump(orderFrame, fw)
    fw.close()
    cur.close()
    conn.close()


def fix_birthday(xbirthday):
    birthdayYear = 1800
    birthdayMonth = 1
    birthdayDay = 1
    birthday = datetime.date(birthdayYear, birthdayMonth, birthdayDay)
    if xbirthday == '' or xbirthday == '<null>':
        return birthday
    else:
        return xbirthday

# def trans(x):
#     for i in x.index:
#         for j in x.columns:
#             x.ix[i,j] = '<null>' if x.ix[i,j] == None else x.ix[i,j]

file = 'orderObj.txt'
fr = open(file,'rb')
orders = pickle.load(fr)

# orders['createtime'] = pd.to_datetime(orders.createtime, format='%Y%m%d')
# orders['createtime'] = orders.createtime.values.astype('datetime64[D]')
# orders['salesorder'] = orders.salesorder.values.astype(str)
# orders['birthday'] = orders['birthday'].where(orders['birthday']!=None, other='<null>')
# print(btdnull.customerid)
# EmptyDel = orders[orders['salesorder'] != '<null>']
# print(EmptyDel.customerid)
# orders['birthday'].apply(fix_birthday)
# print('***********************************************')
# orders.iloc[:,6].map(trans)

print(orders[['birthday', 'tier']].where(orders[['birthday', 'tier']].notnull(), '<null>'))
# print(orders.iloc[:,4].map(trans))
# print(orders.iloc[:,5].map(trans))
fr.close()

# orders['revenue'] = orders.revenue.values.astype('float64')
# print(orders.index)

# for i in range(100):
#     # if orders[i][['birthday'] == "<null>"]:
#     print(orders.iloc[i][['birthday','customername']]) #[['birthday','customername']]

# grouped_month = orders.groupby('createtime')
# grouped_month.revenue.sum().plot()
# grouped_age = orders.groupby('birthday')
# grouped_age.revenue.sum().plot()
# plt.show()


# orderFrame = DataFrame(orders)
#
# orderFrame.rename(columns={0:'part', 1:'storeid', 2:'storename', 3:'customerid', 4:'customername', 5:'birthday',
#                            6:'tier', 7:'club', 8:'salesorder', 9:'createtime', 10:'salestype', 11:'sku',
#                            12:'skuname', 13:'itemtype', 14:'marketprice', 15:'revenue', 16:'quantity', 17:'fst',
#                            18:'fststore', 19:'fstrevenue', 20:'lst', 21:'bcid', 22:'bcname'}, inplace=True)



#     print(type(orders[i].details['createtime']))
#     createtime = int(orders[i].details['createtime'])
#     if(createtime>=20180101 and createtime<=20180201):
#         print(orders[i].details['skuname'])